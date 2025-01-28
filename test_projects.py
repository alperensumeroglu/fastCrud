import asyncio

# An asynchronous function that simulates some work with a delay
async def first_function():
    print("First function started")
    await asyncio.sleep(3)  # Simulates non-blocking delay
    print("First function finished")
    return 5

# Another asynchronous function with its own logic
async def second_function():
    print("Second function started")
    await asyncio.sleep(5)  # Simulates non-blocking delay
    print("Second function finished")
    return 10

# Main asynchronous function that manages tasks
async def main():
    # Create two tasks that will run concurrently
    task1 = asyncio.create_task(first_function())
    task2 = asyncio.create_task(second_function())
    
    # Await the results of the tasks
    result1 = await task1
    result2 = await task2

    # Print the results
    print(f"Result from first function: {result1}")
    print(f"Result from second function: {result2}")

# Entry point of the script
if __name__ == "__main__":
    asyncio.run(main())
