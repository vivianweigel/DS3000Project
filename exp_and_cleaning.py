"""
Project Milestone 2
Group 42
"""
import pandas as pd

def main():
    df = pd.read_csv('lovoo_users.csv')
    print(df.head())

if __name__ == '__main__':
    main()