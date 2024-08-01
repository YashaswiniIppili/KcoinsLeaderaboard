import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scrape_profile(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        coin_count_text = soup.select_one('span.text-14.font-normal.text-light-gray').text.strip()
        if 'point' in coin_count_text:
            coin_count = int(coin_count_text.split(' ')[0])
        else:
            coin_count = int(coin_count_text.replace('points', '').strip())
    except (AttributeError, ValueError):
        coin_count = 0

    return coin_count

def scrape_profiles(profile_dict):
    data = []
    for name, urls in profile_dict.items():
        total_coins = 0
        combined_urls = []
        for url in urls:
            try:
                coins = scrape_profile(url)
                total_coins += coins
                combined_urls.append(url)
                time.sleep(1)  
            except Exception as e:
                logging.error(f"Error scraping {url}: {e}")
        combined_urls_str = ', '.join(combined_urls)
        data.append({'Name': name, 'Profile URLs': combined_urls_str, 'K Coins': total_coins})
    df = pd.DataFrame(data)
    return df

def add_serial_numbers(df):
    df_sorted = df.sort_values(by='K Coins', ascending=False).reset_index(drop=True)
    df_sorted['Serial Number'] = df_sorted.index + 1
    return df_sorted

def main():
    st.title('Product Hunt K-Coins Leaderboard')
    st.header('11 Days Left :)')

    profile_dict = {
        'Yashaswini Ippili': [
            'https://www.producthunt.com/@yashaswini_ippili',
            'https://www.producthunt.com/@zara_bottom', 
            'https://www.producthunt.com/@sahita',
            'https://www.producthunt.com/@sahita1',
            'https://www.producthunt.com/@alcoding',
            'https://www.producthunt.com/@yashish2009'
        ],
        'Ashrita Kumar' : [
            'https://www.producthunt.com/@ashrita_kumar',
            'https://www.producthunt.com/@ashrita_kumar21',
            'https://www.producthunt.com/@ashrita_rao',
        ],
        'Harikrishnan C' : [
            'https://www.producthunt.com/@hari_krishnan38'
        ],
        'Kumar' : [
            'https://www.producthunt.com/@kumrr'
        ],
        'Nikitha' : [
            'https://www.producthunt.com/@nikitha_j_prabhu',
            'https://www.producthunt.com/@niraj_18',
            'https://www.producthunt.com/@nikitha_ni321',
            'https://www.producthunt.com/@jeeksha_krishna',
            'https://www.producthunt.com/@nikitha_prabhu',
            'https://www.producthunt.com/@nikitha_nikki321/followers'
        ],
        'Niranjan' : [
            'https://www.producthunt.com/@niranjan_mogaveera',
            'https://www.producthunt.com/@nirupama_s',
            'https://www.producthunt.com/@girija_srinivas',
            'https://www.producthunt.com/@nirupama_kanchan'
        ],
        'Revanth Reddy' : [
            'https://www.producthunt.com/@revanth_reddy04',
            'https://www.producthunt.com/@reddygaru',
        ],
        'Lohith' : [
            'https://www.producthunt.com/@lohith_ry',
        ],
        'Divya' : [
            'https://www.producthunt.com/@divy_divya_c',
            'https://www.producthunt.com/@divya_c2',
            'https://www.producthunt.com/@disha_divya',
            'https://www.producthunt.com/@sanvi_san',
            'https://www.producthunt.com/@divya_chandrasekharan'
        ],
        'Shreyas' : [
            'https://www.producthunt.com/@shreyas5',
        ],
        'Subham' : [
            'https://www.producthunt.com/@subham_sahu1',
            'https://www.producthunt.com/@subham_sahu2',
            'https://www.producthunt.com/@photu',
            'https://www.producthunt.com/@harsh_here'
        ],
        'Faizulla Shaik' : [
            'https://www.producthunt.com/@faizullashaik',
            'https://www.producthunt.com/@sajidulla_shaik',
            'https://www.producthunt.com/@manoharakumar',
            'https://www.producthunt.com/@shoaib_shaik01',
            'https://www.producthunt.com/@santhosh_muralidharan',
        ],
        'Chetan' : [
            'https://www.producthunt.com/@chethan_m1',
            'https://www.producthunt.com/@ajay42/activity',
            'https://www.producthunt.com/@shivakumar2',
            'https://www.producthunt.com/@chethan_bm',
            'https://www.producthunt.com/@mahadev_bs',
            'https://www.producthunt.com/@nagarathanmma',
        ],
        'Phani' : [
            'https://www.producthunt.com/@phani_slang',
        ],
        'Jayaram Mahale' : [
            'https://www.producthunt.com/@jayaram_mahale',
        ],
        'Vishal' : [
            'https://www.producthunt.com/@vishal_balasubramanian',
        ],
        'Anmol' : [
            'https://www.producthunt.com/@anmol_prakash',
        ],
        'Jayanth' : [
            'https://www.producthunt.com/@jayanthr',
        ],
        'Viana' : [
            'https://www.producthunt.com/@viana_lobo1'
        ],
        'Mihir' : [
            'https://www.producthunt.com/@mihir_srivastava',
        ],
        'Vivek' : [
            'https://www.producthunt.com/@vivek_krz',
        ],
        'Anshaj' : [
            'https://www.producthunt.com/@anshaj_khare',
        ],
        'Abhinav Kumar' : [
            'https://www.producthunt.com/@abhinav_kumar_gupta1',
            'https://www.producthunt.com/@new_user_239210b20f',
            'https://www.producthunt.com/@abhinav23',
            'https://www.producthunt.com/@abhinav_kumar_gupta3',
        ],
        'Padmaja Bhol' : [
            'https://www.producthunt.com/@padmaja_bhol',
        ],
        'Adithya' : [
            'https://www.producthunt.com/@adithya_s4',
        ],
    }

    @st.cache_data(ttl=3600) 
    def get_data():
        logging.info('Scraping profiles...')
        with st.spinner('Scraping profiles...'):  
            data = scrape_profiles(profile_dict)
        logging.info('Scraping completed.')
        return data

    df = get_data()
    if df.empty:
        st.write("No data available")
    else:
        df = add_serial_numbers(df)
        st.dataframe(df[['Serial Number', 'Name', 'Profile URLs', 'K Coins']], hide_index=True)

if __name__ == '__main__':
    main()
