from wp_client import get_site_info, list_pages


def main():
    info = get_site_info()
    print(f"Site: {info['name']} ({info['url']})")
    print("Latest pages:")
    for page_id, title in list_pages():
        print(f"  {page_id}: {title}")


if __name__ == "__main__":
    main()
