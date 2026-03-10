# Top 3 Manufacturers (February 2026)
february_2026_sales = {
    "Toyota": 12272,
    "Suzuki Auto": 6562,
    "Volkswagen Group SA": 4895
}

# Loop through the car brand dictionary
for key, (brand, sales) in enumerate(february_2026_sales.items(), start=1):
    # Display naamsa top three selling car brands for the month of February 2026.
    print(f"{key}. {brand}: {sales} units")