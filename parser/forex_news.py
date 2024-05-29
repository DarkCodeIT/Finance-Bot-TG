import aiohttp, lxml, bs4, asyncio

#Добавил заголовки, иначе выдает ошибку 403 forbiden
headers = {
	"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
	"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}

async def get_data(url: str):

	try:

		async with aiohttp.ClientSession() as session:
			async with session.get(url=url, headers=headers) as response:
				soup = bs4.BeautifulSoup(await response.text(), "lxml")
				main = soup.find("div", class_="flex flex-col").find("div", class_="w-full md:mx-auto md:w-[764px]").find(
					"div", class_="article_WYSIWYG__O0uhw article_articlePage__UMz3q text-[18px] leading-8"
				)

				#Try find link to video
				#Url by default
				video_url = None
				if main.find("div", class_="outerEleWrapper"):
					video_url = main.find("div", class_="outerEleWrapper").find("source").get("src")

				text = None
				if main.find_all("p"):
					code = main.find_all("p")
					text = ""

					for item in code :
						text += f"{item.text}\n"

				#author
				author = soup.find("div", class_="flex flex-col").find("div", class_="text-lg font-semibold leading-7 text-[#181C21]").find('a').text

				date = soup.find("div", class_="flex flex-col").find("div", class_="mt-2 flex flex-col gap-2 text-xs md:mt-2.5 md:gap-2.5").text
				
				data = {
					"author" : author,
					"text" : text,
					"video_link" : video_url,
					"link" : url,
					"date" : date
				}
				return data
	except Exception as ex:
		print(ex)

middle_tasks = []
async def middle_pagination(middle_url: str) -> None:

	try:
		async with aiohttp.ClientSession() as session:
			async with session.get(url=middle_url, headers=headers) as response:
				
				soup = bs4.BeautifulSoup(await response.text(), "lxml")

				tag_div = soup.find("div", id="contentSection").find_all("div", class_="textDiv")

				for item in tag_div:
					link = f"https://ru.investing.com/{item.find("a", class_="title").get("href")}"
					middle_tasks.append(asyncio.create_task(get_data(url=link)))
				print("Middle pagination complete")
	except Exception as ex:
		print(ex)


async def main_pagination(main_url: str) -> list:
	main_tasks = []

	async with aiohttp.ClientSession() as session:
		async with session.get(url=main_url, headers=headers) as response:

			soup = bs4.BeautifulSoup(await response.text(), "lxml")
			tag_a = soup.find(
				"div",
				id="paginationWrap"
			).find(
				"div", class_="midDiv inlineblock"
			).find_all("a")

			main_tasks.append(asyncio.create_task(middle_pagination(middle_url="https://ru.investing.com/analysis/forex")))

			for item in range(2, len(tag_a)):
				link = f"https://ru.investing.com/{tag_a[item].get("href")}"
				main_tasks.append(asyncio.create_task(middle_pagination(middle_url=link)))
				

	print("Main Pagination complete")
	return main_tasks

async def run_script() -> None:
	run_main = await main_pagination(main_url="https://ru.investing.com/analysis/forex/2")
	asyncio.gather(*run_main)
	print("Middle tasks -->")

if __name__ == "__main__":
	asyncio.run(run_script())