
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin


def get_valid_url():
    url = input("\nEnter website URL (or 'q' to quit): ").strip()

    if url.lower() == "q":
        return None

    if not url.startswith(("https://", "http://")):
        url = "https://" + url

    parsed = urlparse(url)

    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        print("Invalid URL. Please enter a valid website address.")
        return ""

    return url


def scrape_website(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; StudentWebScraper/1.0)"
    }

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    for element in soup(["script", "style", "noscript"]):
        element.decompose()

    print("\n" + "=" * 55)
    print("          WEBSITE SCRAPER RESULTS")
    print("=" * 55)
    print(
        "Page title:",
        soup.title.get_text(strip=True) if soup.title else "Not found"
    )
    print("Final URL:", response.url)

    while True:
        print("\nWhat would you like to extract?")
        print("1. Headings")
        print("2. Links")
        print("3. Both headings and links")
        print("4. Enter another website")
        print("5. Exit")

        choice = input("Choose (1-5): ").strip()

        if choice in ("1", "3"):
            headings = soup.find_all(["h1", "h2", "h3"])
            print("\n--- HEADINGS ---")

            if not headings:
                print("No headings found.")
            else:
                for index, heading in enumerate(headings, start=1):
                    text = heading.get_text(" ", strip=True)
                    if text:
                        print(f"{index}. [{heading.name}] {text}")

        if choice in ("2", "3"):
            links = soup.find_all("a", href=True)
            print("\n--- LINKS ---")

            count = 0
            for link in links:
                label = link.get_text(" ", strip=True) or "(No link text)"
                full_url = urljoin(response.url, link["href"])

                if urlparse(full_url).scheme in ("http", "https"):
                    count += 1
                    print(f"{count}. {label}\n   {full_url}")

                    if count >= 30:
                        print("Showing first 30 links only.")
                        break

            if count == 0:
                print("No links found.")

        elif choice == "4":
            return "another"
        elif choice == "5":
            return "exit"
        elif choice not in ("1", "2", "3"):
            print("Invalid choice. Please select 1-5.")


def main():
    print("=" * 55)
    print("             INTERACTIVE WEB SCRAPER")
    print("=" * 55)
    print("Use this tool only on websites you are permitted to access.")

    while True:
        url = get_valid_url()

        if url is None:
            break
        if not url:
            continue

        try:
            result = scrape_website(url)

            if result == "exit":
                break

        except requests.exceptions.Timeout:
            print("The website took too long to respond.")
        except requests.exceptions.HTTPError as error:
            print(f"Website returned an HTTP error: {error}")
        except requests.exceptions.RequestException as error:
            print(f"Could not access the website: {error}")
        except Exception as error:
            print(f"An unexpected error occurred: {error}")

    print("\nThank you for using Interactive Web Scraper!")


if __name__ == "__main__":
    main()
