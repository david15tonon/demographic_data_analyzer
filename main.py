from demographic_data_analyzer import demographic_data_analyzer

def main():
    results = demographic_data_analyzer()

    for key, value in results.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
