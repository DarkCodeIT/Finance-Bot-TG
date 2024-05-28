import aiohttp, lxml, bs4, asyncio

#Добавил заголовки, иначе выдает ошибку 403 forbiden
headers = {
	"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
	"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}

async def get_data(url: str):
	data = {}

	async with aiohttp.ClientSession() as session:
		async with session.get(url=url, headers=headers) as response:
			soup = bs4.BeautifulSoup(await response.text(), "lxml")
			main = soup.find("div", class_="flex flex-col").find("div", class_="w-full md:mx-auto md:w-[764px]").find(
				"div", class_="article_WYSIWYG__O0uhw article_articlePage__UMz3q text-[18px] leading-8"
			)

			#Try find link to video
			if main.find("div", class_="outerEleWrapper"):
				video_url = main.find("div", class_="outerEleWrapper").find("source").get("src")
				print(video_url)

			elif main.find_all("p"):
				text = main.find_all("p")

				for item in text :
					print(item.text())
			


async def middle_pagination(midle_url: str) -> list:
	middle_tasks = []

	async with aiohttp.ClientSession() as session:
		async with session.get(url=midle_url, headers=headers) as response:
			
			soup = bs4.BeautifulSoup(await response.text(), "lxml")

			tag_div = soup.find("div", id="contentSection").find_all("div", class_="textDiv")
			
			for item in tag_div:
				link = f"https://ru.investing.com/{item.find("a", class_="title").get("href")}"
				middle_tasks.append(asyncio.create_task(get_data(url=link)))


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
asyncio.run(get_data(url="https://ru.investing.com/analysis/article-200313191"))