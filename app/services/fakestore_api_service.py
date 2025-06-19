import aiohttp

class FakeStoreApiService:

    def __init__(self, api_url):
        self.api_url = api_url

    async def get_product_by_id(self, product_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.api_url}/products/{product_id}") as response:
                if response.status == 200:
                    return await response.json()
        return None

    async def get_product_list(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.api_url}/products") as response:
                if response.status == 200:
                    return await response.json()
        return None