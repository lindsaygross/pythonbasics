DAYS = [
    # ==================== DAY 1 ====================
    {
        "day": 1,
        "phase": 1,
        "title": "Variables, Types & Conditionals",
        "objectives": [
            "Create variables and understand data types",
            "Use print() to display output",
            "Write if/elif/else statements",
            "Write a basic function",
        ],
        "concepts": [
            {
                "title": "Variables and Types",
                "explanation": "Variables store data. Python has four basic types you need to know: integers (whole numbers), floats (decimals), strings (text), and booleans (True/False). You don't need to declare the type - Python figures it out.",
                "code": '''# Integer - whole numbers
retry_count = 5
max_retries = 10

# Float - decimal numbers
sleep_time = 2.0
success_rate = 0.87

# String - text (use quotes)
error_message = "Server returned 429"
product_name = 'Widget A'

# Boolean - True or False
is_connected = True
has_fallback = False

# Check the type of any variable
print(type(retry_count))   # <class 'int'>
print(type(sleep_time))    # <class 'float'>
print(type(error_message)) # <class 'str'>
print(type(is_connected))  # <class 'bool'>''',
            },
            {
                "title": "Print and F-Strings",
                "explanation": "print() displays output. F-strings (f'...') let you embed variables inside strings. You'll use these constantly in the interview to show your work.",
                "code": '''attempt = 3
max_retries = 5
error = "timeout"

# Basic print
print("Starting API call...")

# F-string - put variables inside curly braces
print(f"Attempt {attempt} of {max_retries}")
print(f"Error: {error}")

# Math inside f-strings
print(f"Remaining attempts: {max_retries - attempt}")

# Multiple variables
product_id = 42
fallback_id = 17
print(f"Product {product_id} falls back to {fallback_id}")''',
            },
            {
                "title": "If / Elif / Else",
                "explanation": "Conditionals let your code make decisions. In the interview, you'll use these to check if you've hit max retries, if a fallback_id is None, or if a product has been visited. Indentation matters in Python - use 4 spaces.",
                "code": '''attempt = 3
max_retries = 5

# Simple if/else
if attempt < max_retries:
    print("Retrying...")
else:
    print("Max retries reached, giving up")

# if/elif/else - checking multiple conditions
status_code = 429

if status_code == 200:
    print("Success!")
elif status_code == 429:
    print("Rate limited - need to sleep")
elif status_code == 500:
    print("Server error - should retry")
else:
    print(f"Unknown status: {status_code}")

# Checking for None (you'll do this A LOT in the interview)
fallback_id = None

if fallback_id is None:
    print("No fallback - end of chain")
else:
    print(f"Next product: {fallback_id}")

# Combining conditions with "and" / "or"
current_id = 5
visited = {1, 2, 3}

if current_id is not None and current_id not in visited:
    print("Haven't visited this product yet")''',
            },
            {
                "title": "Basic Functions",
                "explanation": "Functions group reusable code. You define them with 'def', give them parameters, and they can return values. In the interview you'll write functions like retry_api_call() and get_fallback_chain().",
                "code": '''# Simple function
def greet(name):
    print(f"Hello, {name}!")

greet("Lindsay")  # Hello, Lindsay!

# Function with a return value
def add(a, b):
    return a + b

result = add(3, 7)
print(result)  # 10

# Function with a default parameter
def retry_message(attempt, max_retries=5):
    return f"Attempt {attempt} of {max_retries}"

print(retry_message(1))      # Attempt 1 of 5
print(retry_message(1, 10))  # Attempt 1 of 10

# Function that checks something and returns True/False
def should_retry(attempt, max_retries):
    return attempt < max_retries - 1

print(should_retry(2, 5))  # True
print(should_retry(4, 5))  # False''',
            },
        ],
        "exercises": [
            {
                "title": "Variable Practice",
                "description": "Create variables for an API retry scenario: max_retries (int), sleep_time (float), error_msg (string), and is_success (boolean). Print each one using an f-string.",
                "hint": "Use f-strings like: print(f'Max retries: {max_retries}')",
                "solution": '''max_retries = 5
sleep_time = 2.0
error_msg = "Connection timeout"
is_success = False

print(f"Max retries: {max_retries}")
print(f"Sleep time: {sleep_time} seconds")
print(f"Error: {error_msg}")
print(f"Success: {is_success}")''',
            },
            {
                "title": "Status Code Handler",
                "description": "Write a function called handle_status that takes a status_code parameter. If 200, return 'Success'. If 429, return 'Rate limited'. If 500, return 'Server error'. Otherwise return 'Unknown error'.",
                "hint": "Use if/elif/else inside your function and return a string for each case.",
                "solution": '''def handle_status(status_code):
    if status_code == 200:
        return "Success"
    elif status_code == 429:
        return "Rate limited"
    elif status_code == 500:
        return "Server error"
    else:
        return "Unknown error"

# Test it
print(handle_status(200))   # Success
print(handle_status(429))   # Rate limited
print(handle_status(500))   # Server error
print(handle_status(404))   # Unknown error''',
            },
            {
                "title": "Retry Decision Function",
                "description": "Write a function called should_retry that takes 'attempt' and 'max_retries' as parameters. Return True if the attempt is less than max_retries - 1 (meaning we have retries left). Print the result for attempts 0 through 4 with max_retries=5.",
                "hint": "The condition is: attempt < max_retries - 1. The last attempt (index 4 when max is 5) should return False because we want to raise the error instead of retrying.",
                "solution": '''def should_retry(attempt, max_retries):
    return attempt < max_retries - 1

# Test with max_retries = 5
for i in range(5):
    print(f"Attempt {i}: should_retry = {should_retry(i, 5)}")
# Attempt 0: True  (retry)
# Attempt 1: True  (retry)
# Attempt 2: True  (retry)
# Attempt 3: True  (retry)
# Attempt 4: False (raise the error - last attempt)''',
            },
        ],
        "videos": [
            {"title": "Python Variables & Data Types (Corey Schafer)", "url": "https://www.youtube.com/watch?v=k9TUPpGqYTo"},
            {"title": "If Statements in Python (Corey Schafer)", "url": "https://www.youtube.com/watch?v=DZwmZ8Usvnk"},
            {"title": "Python Functions (CS Dojo)", "url": "https://www.youtube.com/watch?v=9Os0o3wzS_I"},
        ],
        "interview_tip": "In the interview, always name your variables descriptively. 'max_retries' is better than 'n'. The engineer watching you wants to see clean, readable code.",
    },
    # ==================== DAY 2 ====================
    {
        "day": 2,
        "phase": 1,
        "title": "Lists & For Loops",
        "objectives": [
            "Create and manipulate lists",
            "Use for loops and range()",
            "Iterate over lists of data",
            "Use list methods: append, len, indexing",
        ],
        "concepts": [
            {
                "title": "Lists",
                "explanation": "Lists store ordered collections of items. In the interview, the API returns a LIST of product dictionaries. You need to be comfortable creating lists, accessing items by index, and adding items.",
                "code": '''# Creating lists
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
empty_list = []

# Accessing items (0-indexed)
print(numbers[0])   # 1 (first item)
print(numbers[2])   # 3 (third item)
print(numbers[-1])  # 5 (last item)

# Length of a list
print(len(numbers))  # 5

# Adding items
numbers.append(6)
print(numbers)  # [1, 2, 3, 4, 5, 6]

# Checking if something is in a list
print(3 in numbers)   # True
print(99 in numbers)  # False

# A list of product IDs (like in the interview)
product_ids = [101, 102, 103, 104]
chain = []  # Start with empty list, build it up
chain.append(102)
chain.append(103)
print(chain)  # [102, 103]''',
            },
            {
                "title": "For Loops with range()",
                "explanation": "For loops repeat code a set number of times. range(n) gives you numbers 0 through n-1. In the interview, you'll use for loops to iterate through retry attempts and to process lists of products.",
                "code": '''# Basic for loop with range
for i in range(5):
    print(f"Attempt {i}")
# Prints: Attempt 0, Attempt 1, ... Attempt 4

# range(start, stop)
for i in range(1, 6):
    print(i)
# Prints: 1, 2, 3, 4, 5

# INTERVIEW PATTERN: retry loop
max_retries = 5
for attempt in range(max_retries):
    print(f"Try #{attempt + 1} of {max_retries}")
    if attempt < max_retries - 1:
        print("  Will retry...")
    else:
        print("  Last attempt!")''',
            },
            {
                "title": "Looping Over Lists",
                "explanation": "You can loop directly over list items. This is how you'll process the list of products from the API - looping through each product to build the lookup map and compute fallback chains.",
                "code": '''# Loop over items directly
products = ["Widget A", "Widget B", "Widget C"]
for product in products:
    print(f"Processing: {product}")

# Loop with index using enumerate
for i, product in enumerate(products):
    print(f"Product #{i}: {product}")

# INTERVIEW PATTERN: processing a list of product dicts
products = [
    {"id": 1, "name": "Widget A"},
    {"id": 2, "name": "Widget B"},
    {"id": 3, "name": "Widget C"},
]

for product in products:
    print(f"ID: {product['id']}, Name: {product['name']}")

# Building a new list from an existing one
ids = []
for product in products:
    ids.append(product["id"])
print(ids)  # [1, 2, 3]''',
            },
        ],
        "exercises": [
            {
                "title": "Build a Chain",
                "description": "Start with an empty list called 'chain'. Use a for loop with range(1, 6) to append each number to the chain. Print the chain at the end.",
                "hint": "Create chain = [], then loop with for i in range(1, 6): and append i each time.",
                "solution": '''chain = []
for i in range(1, 6):
    chain.append(i)
print(chain)  # [1, 2, 3, 4, 5]''',
            },
            {
                "title": "Extract IDs",
                "description": "Given this list of products, write a for loop that creates a new list containing just the product IDs.\n\nproducts = [{'id': 10, 'name': 'A'}, {'id': 20, 'name': 'B'}, {'id': 30, 'name': 'C'}]",
                "hint": "Access each product's id with product['id'] and append it to a new list.",
                "solution": '''products = [{"id": 10, "name": "A"}, {"id": 20, "name": "B"}, {"id": 30, "name": "C"}]

ids = []
for product in products:
    ids.append(product["id"])
print(ids)  # [10, 20, 30]''',
            },
            {
                "title": "Retry Counter",
                "description": "Write a for loop that simulates 5 retry attempts. For each attempt, print 'Attempt X: retrying...' except for the last one, which should print 'Attempt X: FINAL attempt'. Use max_retries = 5.",
                "hint": "Use range(max_retries) and check if attempt < max_retries - 1 to decide which message to print.",
                "solution": '''max_retries = 5
for attempt in range(max_retries):
    if attempt < max_retries - 1:
        print(f"Attempt {attempt}: retrying...")
    else:
        print(f"Attempt {attempt}: FINAL attempt")''',
            },
        ],
        "videos": [
            {"title": "Python Lists (Corey Schafer)", "url": "https://www.youtube.com/watch?v=W8KRzm-HUcc"},
            {"title": "For Loops in Python (CS Dojo)", "url": "https://www.youtube.com/watch?v=OnDr4J2UJ8s"},
        ],
        "interview_tip": "When you get the list of products back from the API, say out loud: 'I have a list of product dictionaries. Let me iterate through them to build my lookup map.' This shows the interviewer you're thinking clearly.",
    },
    # ==================== DAY 3 ====================
    {
        "day": 3,
        "phase": 1,
        "title": "Dictionaries (THE Key Skill)",
        "objectives": [
            "Create and access dictionaries",
            "Use .get() for safe access",
            "Loop through dictionaries with .items()",
            "Build a lookup dictionary from a list - THE critical interview pattern",
        ],
        "concepts": [
            {
                "title": "Dictionary Basics",
                "explanation": "A dictionary maps keys to values, like a real dictionary maps words to definitions. In the interview, you'll use dictionaries EVERYWHERE: each product is a dictionary, and you'll build a lookup map (dictionary) from product IDs to product objects.",
                "code": '''# Creating a dictionary
product = {
    "id": 1,
    "name": "Widget A",
    "fallback_id": 2
}

# Accessing values by key
print(product["id"])           # 1
print(product["name"])         # Widget A
print(product["fallback_id"])  # 2

# Adding a new key
product["related_items"] = [2, 3]
print(product)

# Checking if a key exists
print("id" in product)       # True
print("price" in product)    # False''',
            },
            {
                "title": "Safe Access with .get()",
                "explanation": ".get() lets you access a key without crashing if it doesn't exist. You can provide a default value. This is CRITICAL in the interview for handling products that might not have a fallback_id or when looking up products that might not exist in your map.",
                "code": '''product = {"id": 1, "name": "Widget A", "fallback_id": 2}

# .get() returns None if key doesn't exist (no crash!)
print(product.get("fallback_id"))  # 2
print(product.get("price"))        # None (no crash)

# .get() with a default value
print(product.get("price", 0))     # 0 (default)
print(product.get("name", "Unknown"))  # Widget A (key exists)

# WHY THIS MATTERS IN THE INTERVIEW:
product_map = {1: {"id": 1}, 2: {"id": 2}}

# This would CRASH if product 99 doesn't exist:
# product_map[99]  # KeyError!

# This is SAFE:
result = product_map.get(99)  # None, no crash
print(result)

# Use it to safely get the next product in a chain
current_id = 99
next_product = product_map.get(current_id)
if next_product is None:
    print("Product not found - end of chain")''',
            },
            {
                "title": "Looping Through Dictionaries",
                "explanation": "You can loop through keys, values, or both. The .items() method gives you key-value pairs. You'll use this to iterate through your product map.",
                "code": '''product = {"id": 1, "name": "Widget A", "fallback_id": 2}

# Loop through keys
for key in product:
    print(key)  # id, name, fallback_id

# Loop through values
for value in product.values():
    print(value)  # 1, Widget A, 2

# Loop through key-value pairs (MOST USEFUL)
for key, value in product.items():
    print(f"{key}: {value}")

# Real example: print all products in a map
product_map = {
    1: {"id": 1, "name": "Widget A"},
    2: {"id": 2, "name": "Widget B"},
}

for product_id, product in product_map.items():
    print(f"Product {product_id}: {product['name']}")''',
            },
            {
                "title": "Building a Lookup Map (INTERVIEW CRITICAL)",
                "explanation": "THIS is the single most important pattern for your interview. The API gives you a LIST of products. You need to convert it to a DICTIONARY (map) where the key is the product ID and the value is the product itself. This gives you O(1) lookup instead of searching through the whole list.",
                "code": '''# The API returns a LIST of products
products = [
    {"id": 1, "name": "Widget A", "fallback_id": 2},
    {"id": 2, "name": "Widget B", "fallback_id": 3},
    {"id": 3, "name": "Widget C", "fallback_id": None},
]

# BUILD THE LOOKUP MAP
# Key = product id, Value = the product dictionary
product_map = {}
for product in products:
    product_map[product["id"]] = product

# Now you can instantly look up any product by ID!
print(product_map[1])  # {"id": 1, "name": "Widget A", "fallback_id": 2}
print(product_map[2])  # {"id": 2, "name": "Widget B", "fallback_id": 3}

# Say this out loud in the interview:
# "I'm building a hashmap from product ID to product
#  for O(1) lookup instead of searching the list"

# Without the map, finding product 2 requires searching:
# for p in products:
#     if p["id"] == 2:  # O(n) - slow!

# With the map, it's instant:
# product_map[2]  # O(1) - fast!''',
            },
        ],
        "exercises": [
            {
                "title": "Product Dictionary",
                "description": "Create a dictionary for a product with keys: 'id' (integer), 'name' (string), 'fallback_id' (integer or None). Print each value using both bracket notation and .get().",
                "hint": "product = {'id': 1, 'name': 'Widget', 'fallback_id': 2}",
                "solution": '''product = {"id": 1, "name": "Widget A", "fallback_id": 2}

# Bracket notation
print(product["id"])           # 1
print(product["name"])         # Widget A
print(product["fallback_id"])  # 2

# .get() notation
print(product.get("id"))           # 1
print(product.get("name"))         # Widget A
print(product.get("fallback_id"))  # 2
print(product.get("price"))        # None (doesn't exist)
print(product.get("price", 0))     # 0 (with default)''',
            },
            {
                "title": "Build a Lookup Map",
                "description": "Given this list of products, build a product_map dictionary where each key is the product's id and each value is the product dictionary. Then look up product with id 2 and print its name.\n\nproducts = [{'id': 1, 'name': 'A', 'fallback_id': 2}, {'id': 2, 'name': 'B', 'fallback_id': 3}, {'id': 3, 'name': 'C', 'fallback_id': None}]",
                "hint": "Loop through products. For each product, set product_map[product['id']] = product",
                "solution": '''products = [
    {"id": 1, "name": "A", "fallback_id": 2},
    {"id": 2, "name": "B", "fallback_id": 3},
    {"id": 3, "name": "C", "fallback_id": None},
]

product_map = {}
for product in products:
    product_map[product["id"]] = product

# Look up product 2
print(product_map[2]["name"])  # B''',
            },
            {
                "title": "Safe Chain Following",
                "description": "Given a product_map, write code that starts with product 1, gets its fallback_id, looks up that product in the map (safely with .get()), and prints the fallback product's name. Handle the case where the fallback product doesn't exist in the map.",
                "hint": "Get fallback_id from the product, then use product_map.get(fallback_id) to safely look it up.",
                "solution": '''product_map = {
    1: {"id": 1, "name": "Widget A", "fallback_id": 2},
    2: {"id": 2, "name": "Widget B", "fallback_id": 3},
}

# Start with product 1
current = product_map[1]
fallback_id = current["fallback_id"]

# Safely look up the fallback
fallback_product = product_map.get(fallback_id)
if fallback_product is not None:
    print(f"Fallback: {fallback_product['name']}")
else:
    print("Fallback product not found in map")''',
            },
        ],
        "videos": [
            {"title": "Python Dictionaries (Corey Schafer)", "url": "https://www.youtube.com/watch?v=daefaLgNkw0"},
            {"title": "Python Dictionaries Explained (Tech With Tim)", "url": "https://www.youtube.com/watch?v=XCcpzWs-CI4"},
        ],
        "interview_tip": "When you build the lookup map in the interview, say: 'I'm building a hashmap from product ID to product for O(1) lookup instead of searching the list each time.' This shows you understand time complexity.",
    },
    # ==================== DAY 4 ====================
    {
        "day": 4,
        "phase": 1,
        "title": "Sets & While Loops",
        "objectives": [
            "Understand sets and membership checking",
            "Use sets for cycle detection",
            "Write while loops with conditions",
            "Combine while loops with sets (the DFS pattern)",
        ],
        "concepts": [
            {
                "title": "Sets",
                "explanation": "A set is an unordered collection of UNIQUE items. The key operation is checking membership with 'in', which is O(1) - instant. In the interview, you'll use a visited set to detect cycles in the fallback chain.",
                "code": '''# Creating a set
visited = set()

# Adding items
visited.add(1)
visited.add(2)
visited.add(3)
print(visited)  # {1, 2, 3}

# Adding a duplicate does nothing
visited.add(1)
print(visited)  # {1, 2, 3} - still only 3 items

# THE KEY OPERATION: checking membership
print(1 in visited)   # True  - O(1) instant!
print(99 in visited)  # False - O(1) instant!

# Compare with checking a list (slow for large lists)
# 1 in [1, 2, 3, 4, ...]  # O(n) - has to check each item
# 1 in {1, 2, 3, 4, ...}  # O(1) - instant hash lookup''',
            },
            {
                "title": "While Loops",
                "explanation": "A while loop keeps running as long as its condition is True. In the interview, you'll use a while loop for DFS - keep following the fallback chain WHILE there's a next product AND you haven't visited it.",
                "code": '''# Basic while loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# While loop with a condition that changes
current_id = 1
while current_id is not None:
    print(f"Visiting product {current_id}")
    # Simulate moving to next product
    if current_id < 3:
        current_id += 1
    else:
        current_id = None  # End of chain

# DANGER: infinite loops!
# while True:
#     print("This never stops!")
# Always make sure your condition will eventually become False''',
            },
            {
                "title": "Cycle Detection Pattern (INTERVIEW CRITICAL)",
                "explanation": "When following a fallback chain, products might form a cycle (A -> B -> A). Without cycle detection, your code loops forever. The pattern: keep a visited set, check before visiting, stop if already visited.",
                "code": '''# CYCLE DETECTION with visited set
# Imagine: product 1 -> 2 -> 3 -> 1 (cycle!)

visited = set()
chain = [1, 2, 3, 1, 2, 3]  # What we'd visit without detection

# With cycle detection:
visited = set()
for product_id in chain:
    if product_id in visited:
        print(f"CYCLE DETECTED: {product_id} already visited!")
        break
    visited.add(product_id)
    print(f"Visiting {product_id}")

# Output:
# Visiting 1
# Visiting 2
# Visiting 3
# CYCLE DETECTED: 1 already visited!

# THE INTERVIEW PATTERN: while loop + visited set
current_id = 1
visited = set()

# Keep going while we have a product AND haven't seen it
while current_id is not None and current_id not in visited:
    visited.add(current_id)
    print(f"Processing product {current_id}")
    # In the real code, you'd look up the next fallback_id here
    current_id = current_id + 1 if current_id < 3 else 1  # Simulates a cycle

print(f"Stopped. Visited: {visited}")''',
            },
        ],
        "exercises": [
            {
                "title": "Visited Set Practice",
                "description": "Create an empty set called 'visited'. Loop through the list [1, 2, 3, 2, 4, 1, 5] and for each number: if it's already in visited, print 'Already visited X'. Otherwise, add it to visited and print 'Visiting X'.",
                "hint": "Use 'if x in visited' to check membership, and visited.add(x) to add.",
                "solution": '''visited = set()
numbers = [1, 2, 3, 2, 4, 1, 5]

for num in numbers:
    if num in visited:
        print(f"Already visited {num}")
    else:
        visited.add(num)
        print(f"Visiting {num}")''',
            },
            {
                "title": "While Loop Chain",
                "description": "Write a while loop that starts with current = 1 and keeps going while current <= 5. Each iteration, print the current value and increment by 1. After the loop, print 'Done'.",
                "hint": "while current <= 5: print, then current += 1",
                "solution": '''current = 1
while current <= 5:
    print(f"Current: {current}")
    current += 1
print("Done")''',
            },
            {
                "title": "Detect the Cycle",
                "description": "Given this chain dictionary where each key points to the next ID, use a while loop and visited set to follow the chain starting from ID 1. Print each ID you visit and stop when you detect a cycle.\n\nnext_map = {1: 2, 2: 3, 3: 4, 4: 2}  (4 points back to 2 = cycle)",
                "hint": "Start with current_id = 1 and visited = set(). While current_id is not None and not in visited, add to visited, print it, then get next from next_map.get(current_id).",
                "solution": '''next_map = {1: 2, 2: 3, 3: 4, 4: 2}

current_id = 1
visited = set()

while current_id is not None and current_id not in visited:
    visited.add(current_id)
    print(f"Visiting: {current_id}")
    current_id = next_map.get(current_id)

if current_id is not None:
    print(f"Cycle detected at: {current_id}")
else:
    print("Chain ended (no cycle)")''',
            },
        ],
        "videos": [
            {"title": "Python Sets (Corey Schafer)", "url": "https://www.youtube.com/watch?v=r3R3h5ly_30"},
            {"title": "While Loops in Python (CS Dojo)", "url": "https://www.youtube.com/watch?v=6TEGxJXLAWQ"},
        ],
        "interview_tip": "When you add the visited set, say: 'I'm using a visited set to detect cycles in the fallback chain. Set membership checking is O(1) so this doesn't add overhead.'",
    },
    # ==================== DAY 5 ====================
    {
        "day": 5,
        "phase": 1,
        "title": "Try/Except & Time.Sleep",
        "objectives": [
            "Understand exceptions and error handling",
            "Write try/except blocks",
            "Learn the absorb vs throw pattern",
            "Use time.sleep() for retry delays",
        ],
        "concepts": [
            {
                "title": "Exceptions",
                "explanation": "When something goes wrong in Python, it 'raises' an exception. If you don't handle it, your program crashes. In the interview, the API server raises exceptions (429 errors, random errors), and YOUR job is to catch them and retry.",
                "code": '''# This would crash your program:
# result = 10 / 0  # ZeroDivisionError!
# product_map[99]  # KeyError!

# try/except CATCHES the error so your program doesn't crash
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Caught an error: {e}")

print("Program keeps running!")

# Catching any exception
try:
    product_map = {}
    value = product_map[99]
except Exception as e:
    print(f"Error: {e}")
    print(f"Error type: {type(e).__name__}")''',
            },
            {
                "title": "Absorb vs Throw Pattern (INTERVIEW CRITICAL)",
                "explanation": "In the retry logic, you need two behaviors: (1) ABSORB the error on non-final attempts (catch it, print it, sleep, try again), (2) THROW the error on the final attempt (let it crash - you've used all retries). The key check: if attempt < max_retries - 1, absorb; otherwise, raise.",
                "code": '''# THE ABSORB vs THROW PATTERN
max_retries = 5

for attempt in range(max_retries):
    try:
        # Simulate an API call that fails
        raise Exception("Server error 500")
    except Exception as e:
        if attempt < max_retries - 1:
            # ABSORB: we have retries left
            print(f"Attempt {attempt} failed: {e}")
            print("  Retrying...")
        else:
            # THROW: no retries left, give up
            print(f"Attempt {attempt} failed: {e}")
            print("  No more retries!")
            raise  # re-raises the same exception

# 'raise' without arguments re-raises the current exception
# This is exactly what you do in the interview''',
            },
            {
                "title": "time.sleep() for Retry Delays",
                "explanation": "time.sleep(n) pauses your program for n seconds. In the interview, the server rate-limits requests within a 2-second window, so sleeping 2 seconds between retries clears the rate limit.",
                "code": '''import time

# Sleep for 2 seconds
print("Starting...")
time.sleep(2)
print("2 seconds later!")

# In the interview context:
# The server returns 429 if you call too fast
# The rate limit window is random, max 2 seconds
# So time.sleep(2) guarantees you clear the window

# Say this out loud:
# "I'm sleeping 2 seconds because the server rate limits
#  within a random window up to 2 seconds"

# Full retry with sleep:
import time

max_retries = 3
sleep_time = 2

for attempt in range(max_retries):
    try:
        print(f"Attempt {attempt}...")
        # In real code: result = api_function()
        raise Exception("API Error")  # simulating failure
    except Exception as e:
        if attempt < max_retries - 1:
            print(f"  Failed: {e}. Sleeping {sleep_time}s...")
            time.sleep(sleep_time)
        else:
            print(f"  Final attempt failed: {e}")
            raise''',
            },
        ],
        "exercises": [
            {
                "title": "Basic Try/Except",
                "description": "Write a try/except block that tries to convert the string 'hello' to an integer (int('hello')). Catch the ValueError and print a friendly error message.",
                "hint": "try: int('hello') except ValueError as e: print(...)",
                "solution": '''try:
    number = int("hello")
except ValueError as e:
    print(f"Could not convert to int: {e}")

print("Program continues!")''',
            },
            {
                "title": "Absorb vs Throw",
                "description": "Write a for loop with 4 attempts (range(4)). In each attempt, raise an Exception('API failed'). For the first 3 attempts, absorb the error (print it and continue). On the 4th attempt (index 3), re-raise it.",
                "hint": "Check if attempt < 3 to decide absorb vs throw. Use 'raise' to re-raise.",
                "solution": '''max_retries = 4

for attempt in range(max_retries):
    try:
        raise Exception("API failed")
    except Exception as e:
        if attempt < max_retries - 1:
            print(f"Attempt {attempt}: {e} - absorbing, will retry")
        else:
            print(f"Attempt {attempt}: {e} - throwing!")
            raise''',
            },
        ],
        "videos": [
            {"title": "Python Try/Except (Corey Schafer)", "url": "https://www.youtube.com/watch?v=NIWwJbo-9_8"},
            {"title": "Python Time Module", "url": "https://www.youtube.com/watch?v=Iu3-BYm9Klg"},
        ],
        "interview_tip": "The absorb/throw pattern is the CORE of Part 1. Practice until you can write it from memory without thinking.",
    },
    # ==================== DAY 6 ====================
    {
        "day": 6,
        "phase": 1,
        "title": "Build the API Retry Logic",
        "objectives": [
            "Write the complete retry_api_call function",
            "Understand why 5 retries and 2-second sleep",
            "Practice the pattern from memory",
        ],
        "concepts": [
            {
                "title": "The Complete Retry Function",
                "explanation": "This is the EXACT function you'll write in Part 1 of the interview. It wraps any API call in retry logic with try/except, for loop, and time.sleep. Memorize this pattern.",
                "code": '''import time

def retry_api_call(api_function, max_retries=5, sleep_time=2):
    """Call api_function with retry logic."""
    for attempt in range(max_retries):
        try:
            result = api_function()
            return result  # Success! Return the data
        except Exception as e:
            if attempt < max_retries - 1:
                # ABSORB: print error, sleep, retry
                print(f"Attempt {attempt + 1} failed: {e}")
                time.sleep(sleep_time)
            else:
                # THROW: no retries left
                raise  # Re-raise the exception

# Usage:
# products = retry_api_call(get_products)''',
            },
            {
                "title": "Why 5 Retries?",
                "explanation": "The server has a 67% chance of error on any single call (2/3 failure rate). The probability that ALL 5 attempts fail is (2/3)^5 = ~13%. So 5 retries gives ~87% success rate. Say this math out loud in the interview!",
                "code": '''# The math behind 5 retries:
failure_rate = 2/3  # 67% chance of failure per call

for num_retries in range(1, 8):
    all_fail = failure_rate ** num_retries
    success = 1 - all_fail
    print(f"{num_retries} retries: {success:.1%} success rate")

# Output:
# 1 retries: 33.3% success
# 2 retries: 55.6% success
# 3 retries: 70.4% success
# 4 retries: 80.2% success
# 5 retries: 86.8% success  <-- good enough!
# 6 retries: 91.2% success
# 7 retries: 94.2% success

# SAY IN INTERVIEW:
# "I'll retry 5 times because with a 67% failure rate,
#  (2/3)^5 gives about 13% chance all five fail,
#  so roughly 87% success rate"''',
            },
            {
                "title": "Why 2-Second Sleep?",
                "explanation": "The server tracks when the last API call was made. If another request comes in too quickly, it returns a 429 (rate limit error). The random window is at most 2 seconds, so sleeping 2 seconds guarantees you're past the rate limit window.",
                "code": '''# The server does something like this internally:
# last_call_time = time.time()
# rate_limit_window = random.random() * 2  # 0 to 2 seconds
#
# if time.time() - last_call_time < rate_limit_window:
#     raise Exception("429 Too Many Requests")

# So if you sleep 2 seconds, you're GUARANTEED to be
# past the rate limit window (which is at most 2 seconds)

# SAY IN INTERVIEW:
# "I'm sleeping 2 seconds because the server rate limits
#  within a random window up to 2 seconds, so a 2-second
#  sleep guarantees we clear the window"''',
            },
        ],
        "exercises": [
            {
                "title": "Write Retry From Memory",
                "description": "Without looking at the example, write the complete retry_api_call function. It should take api_function, max_retries=5, and sleep_time=2 as parameters. Use for loop, try/except, absorb/throw pattern, and time.sleep.",
                "hint": "Structure: def -> for loop -> try -> call function -> return result -> except -> if not last attempt: print + sleep -> else: raise",
                "solution": '''import time

def retry_api_call(api_function, max_retries=5, sleep_time=2):
    for attempt in range(max_retries):
        try:
            result = api_function()
            return result
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"Attempt {attempt + 1} failed: {e}")
                time.sleep(sleep_time)
            else:
                raise''',
            },
            {
                "title": "Test Your Retry Logic",
                "description": "Write a fake API function that fails 3 times then succeeds. Use a global counter. Then call it with your retry function.",
                "hint": "Use a list with one element as a counter (to modify in the nested function), increment it each call, raise if < 3.",
                "solution": '''import time

call_count = [0]

def flaky_api():
    call_count[0] += 1
    if call_count[0] < 4:
        raise Exception(f"Error on call {call_count[0]}")
    return [{"id": 1, "name": "Widget A"}]

def retry_api_call(api_function, max_retries=5, sleep_time=0.1):
    for attempt in range(max_retries):
        try:
            result = api_function()
            return result
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"Attempt {attempt + 1} failed: {e}")
                time.sleep(sleep_time)
            else:
                raise

# Test it
products = retry_api_call(flaky_api)
print(f"Success! Got: {products}")''',
            },
        ],
        "videos": [
            {"title": "API Error Handling in Python", "url": "https://www.youtube.com/watch?v=HQp1OHDm5Fc"},
        ],
        "interview_tip": "Part 1 is the warmup. Get through it FAST to unlock Part 2 where the real problem is. Practice until you can write this function in under 3 minutes.",
    },
    # ==================== DAY 7 ====================
    {
        "day": 7,
        "phase": 1,
        "title": "Phase 1 Checkpoint",
        "objectives": [
            "Write all Phase 1 patterns from memory",
            "Self-assess your readiness",
            "Identify weak spots for extra practice",
        ],
        "concepts": [
            {
                "title": "Checkpoint: Everything You Should Know",
                "explanation": "Today is about testing yourself. You should be able to write ALL of the following without looking at notes. Go through each one and check your confidence.",
                "code": '''# CHECKLIST - Can you write these from memory?

# 1. Variables and types
max_retries = 5        # int
sleep_time = 2.0       # float
message = "error"      # string
success = True         # bool

# 2. F-strings
print(f"Retry {max_retries} times, sleep {sleep_time}s")

# 3. If/elif/else
if success:
    print("Done!")
elif max_retries > 0:
    print("Retrying...")
else:
    print("Failed")

# 4. Lists and for loops
items = [1, 2, 3]
for item in items:
    print(item)

# 5. Dictionaries and .get()
product = {"id": 1, "fallback_id": 2}
fid = product.get("fallback_id")

# 6. Building a lookup map
products = [{"id": 1}, {"id": 2}]
product_map = {}
for p in products:
    product_map[p["id"]] = p

# 7. Sets and membership
visited = set()
visited.add(1)
print(1 in visited)  # True

# 8. While loop with cycle detection
current_id = 1
while current_id is not None and current_id not in visited:
    visited.add(current_id)
    current_id = None  # simplified

# 9. Try/except with absorb/throw
import time
for attempt in range(5):
    try:
        pass  # api call here
    except Exception as e:
        if attempt < 4:
            time.sleep(2)
        else:
            raise''',
            },
        ],
        "exercises": [
            {
                "title": "Full Retry Function (From Memory)",
                "description": "Write the complete retry_api_call function from memory. No peeking at previous days! Include: import time, function definition with default parameters, for loop, try/except, absorb/throw pattern, time.sleep.",
                "hint": "If you're stuck, go back to Day 6 and study it more, then try again tomorrow.",
                "solution": '''import time

def retry_api_call(api_function, max_retries=5, sleep_time=2):
    for attempt in range(max_retries):
        try:
            result = api_function()
            return result
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"Attempt {attempt + 1} failed: {e}")
                time.sleep(sleep_time)
            else:
                raise''',
            },
            {
                "title": "Build Lookup Map (From Memory)",
                "description": "Given a list of product dicts with 'id' and 'fallback_id' keys, build a lookup map. Do it from memory.",
                "hint": "product_map = {} then loop through products, mapping product['id'] -> product",
                "solution": '''products = [
    {"id": 1, "fallback_id": 2},
    {"id": 2, "fallback_id": 3},
    {"id": 3, "fallback_id": None},
]

product_map = {}
for product in products:
    product_map[product["id"]] = product

# Verify
for pid, p in product_map.items():
    print(f"ID {pid}: fallback -> {p['fallback_id']}")''',
            },
            {
                "title": "Cycle Detection (From Memory)",
                "description": "Write a while loop that follows a chain of IDs using a dictionary lookup. Use a visited set to detect cycles. Start from ID 1.\n\nchain_map = {1: 2, 2: 3, 3: 1}  (cycle: 3 points back to 1)",
                "hint": "While current_id is not None AND not in visited: add to visited, look up next ID with .get()",
                "solution": '''chain_map = {1: 2, 2: 3, 3: 1}

current_id = 1
visited = set()
path = []

while current_id is not None and current_id not in visited:
    visited.add(current_id)
    path.append(current_id)
    current_id = chain_map.get(current_id)

print(f"Path: {path}")
if current_id is not None:
    print(f"Cycle detected at: {current_id}")''',
            },
        ],
        "videos": [],
        "interview_tip": "If you can write all three exercises above from memory, you're ready for Phase 2. If not, spend another day on the concepts you're weakest on.",
    },
    # ==================== DAY 8 ====================
    {
        "day": 8,
        "phase": 2,
        "title": "Understanding the Full Interview Problem",
        "objectives": [
            "Understand the complete interview structure (Parts 1-3)",
            "Read the server code and understand what it does",
            "Write pseudocode for the full solution",
        ],
        "concepts": [
            {
                "title": "The Big Picture",
                "explanation": "The interview has 3 parts. Part 1: Write retry logic for a flaky API (you've mastered this). Part 2: Take the product data, build a lookup map, then use DFS to follow fallback chains. Part 3 (stretch): Connect related products. Let's understand the full flow.",
                "code": '''# THE FULL INTERVIEW FLOW:

# PART 1: Call the API with retry logic
# - Server is unreliable (67% error rate + rate limiting)
# - You write client-side retry with try/except
# - Result: you get a list of product dictionaries

# PART 2: Process the products
# Step A: Build a lookup map (dict from id -> product)
# Step B: For each product, follow its fallback chain using DFS
# Step C: Store the chain as "related_items" on each product

# PART 3 (stretch): Connected components
# If product 1 chains to 2 and 3, then 2 and 3 should
# also have 1 in their related_items

# Example product data from the API:
products = [
    {"id": 1, "name": "Basic Widget",    "fallback_id": 2},
    {"id": 2, "name": "Pro Widget",      "fallback_id": 3},
    {"id": 3, "name": "Premium Widget",  "fallback_id": None},
    {"id": 4, "name": "Gadget A",        "fallback_id": 5},
    {"id": 5, "name": "Gadget B",        "fallback_id": None},
]

# Product 1 -> 2 -> 3 -> None (chain: [2, 3])
# Product 2 -> 3 -> None (chain: [3])
# Product 3 -> None (chain: [])
# Product 4 -> 5 -> None (chain: [5])
# Product 5 -> None (chain: [])''',
            },
            {
                "title": "Pseudocode for Full Solution",
                "explanation": "Before writing code, write pseudocode. This is what you should do in the interview too - talk through your plan before coding.",
                "code": '''# PSEUDOCODE FOR THE FULL SOLUTION

# Part 1:
# def retry_api_call(api_function, max_retries=5, sleep=2):
#     for each attempt:
#         try: call function, return result
#         except: if not last attempt, sleep and retry
#                 if last attempt, raise

# Part 2:
# def process_products(api_function):
#     Step 1: products = retry_api_call(api_function)
#
#     Step 2: Build lookup map
#         product_map = {}
#         for each product in products:
#             product_map[product.id] = product
#
#     Step 3: For each product, find its fallback chain
#         for each product in products:
#             chain = get_fallback_chain(product, product_map)
#             product.related_items = chain
#
#     return products

# def get_fallback_chain(product, product_map):
#     chain = []
#     visited = set()
#     current_id = product.fallback_id
#     while current_id is not None and not in visited:
#         add current_id to visited
#         add current_id to chain
#         look up current_id in product_map
#         if not found, break
#         current_id = next product's fallback_id
#     return chain''',
            },
        ],
        "exercises": [
            {
                "title": "Trace Through the Problem",
                "description": "Given these products, trace through by hand what the fallback chain (related_items) should be for EACH product:\n\nProduct 1 (fallback_id: 2)\nProduct 2 (fallback_id: 3)\nProduct 3 (fallback_id: None)\nProduct 4 (fallback_id: 5)\nProduct 5 (fallback_id: 4) <-- cycle!",
                "hint": "Follow each chain step by step. Product 5 -> 4 -> 5 is a cycle, so stop when you revisit.",
                "solution": '''# Product 1: follow 1 -> 2 -> 3 -> None
#   related_items = [2, 3]

# Product 2: follow 2 -> 3 -> None
#   related_items = [3]

# Product 3: follow 3 -> None
#   related_items = []

# Product 4: follow 4 -> 5 -> 4 (CYCLE at 4!)
#   related_items = [5]

# Product 5: follow 5 -> 4 -> 5 (CYCLE at 5!)
#   related_items = [4]''',
            },
            {
                "title": "Write Pseudocode",
                "description": "Write pseudocode (in comments) for the get_fallback_chain function. Include: initialization of chain and visited set, while loop condition, what happens inside the loop, and when to break.",
                "hint": "Think about: What do you initialize? What's the while condition? What do you do each iteration? When do you stop?",
                "solution": '''# def get_fallback_chain(product, product_map):
#     create empty chain list
#     create empty visited set
#     current_id = product's fallback_id
#
#     while current_id is not None AND current_id not in visited:
#         add current_id to visited set
#         add current_id to chain list
#         look up current_id in product_map using .get()
#         if product not found in map:
#             break (missing product, end of chain)
#         current_id = the looked-up product's fallback_id
#
#     return chain''',
            },
        ],
        "videos": [
            {"title": "Graph Traversal Explained (CS Dojo)", "url": "https://www.youtube.com/watch?v=pcKY4hjDrxk"},
        ],
        "interview_tip": "Start the interview by saying: 'Let me read through the server code to understand the error patterns, then I'll write my plan before coding.' This shows maturity.",
    },
    # ==================== DAY 9 ====================
    {
        "day": 9,
        "phase": 2,
        "title": "DFS: Following the Fallback Chain",
        "objectives": [
            "Write the get_fallback_chain function",
            "Handle all edge cases: None, cycles, missing products",
            "Practice tracing through examples",
        ],
        "concepts": [
            {
                "title": "Iterative DFS (The Core Algorithm)",
                "explanation": "DFS (Depth-First Search) means following a path as deep as it goes before backtracking. Here, the path is the fallback chain. Alex specifically said to use ITERATIVE DFS (while loop), NOT recursion.",
                "code": '''def get_fallback_chain(product, product_map):
    """Follow the fallback chain for a product.
    Returns a list of product IDs in the chain."""
    chain = []
    visited = set()
    current_id = product.get("fallback_id")

    while current_id is not None and current_id not in visited:
        visited.add(current_id)
        chain.append(current_id)
        # Look up the next product in our map
        fallback_product = product_map.get(current_id)
        if fallback_product is None:
            break  # Product not in map, end of chain
        current_id = fallback_product.get("fallback_id")

    return chain

# Test it:
products = [
    {"id": 1, "fallback_id": 2},
    {"id": 2, "fallback_id": 3},
    {"id": 3, "fallback_id": None},
]

product_map = {}
for p in products:
    product_map[p["id"]] = p

# Test each product
for p in products:
    chain = get_fallback_chain(p, product_map)
    print(f"Product {p['id']} chain: {chain}")

# Output:
# Product 1 chain: [2, 3]
# Product 2 chain: [3]
# Product 3 chain: []''',
            },
            {
                "title": "Edge Cases",
                "explanation": "The interviewer will test edge cases. Here's every case you need to handle:",
                "code": '''# Edge Case 1: No fallback (fallback_id is None)
product = {"id": 3, "fallback_id": None}
# Result: chain = [] (while loop never enters)

# Edge Case 2: Cycle (A -> B -> A)
products = [
    {"id": 1, "fallback_id": 2},
    {"id": 2, "fallback_id": 1},  # Points back to 1!
]
# Product 1: visits 2, then tries 1 but 1... wait,
# we only add FALLBACK IDs to visited. Let me trace:
# current_id starts at 2 (product 1's fallback)
# 2 not in visited -> add 2, chain=[2], look up 2, next=1
# 1 not in visited -> add 1, chain=[2,1], look up 1, next=2
# 2 IS in visited -> STOP
# Result: chain = [2, 1]

# Edge Case 3: Product points to itself
products = [{"id": 1, "fallback_id": 1}]
# current_id = 1
# 1 not in visited -> add 1, chain=[1], look up 1, next=1
# 1 IS in visited -> STOP
# Result: chain = [1]

# Edge Case 4: Fallback points to non-existent product
products = [{"id": 1, "fallback_id": 99}]
# product_map only has {1: ...}
# current_id = 99
# 99 not in visited -> add 99, chain=[99]
# product_map.get(99) returns None -> break
# Result: chain = [99]''',
            },
        ],
        "exercises": [
            {
                "title": "Write DFS From Memory",
                "description": "Write the get_fallback_chain function from memory. It takes a product dict and product_map dict. Returns a list of IDs in the fallback chain.",
                "hint": "Initialize chain=[], visited=set(), current_id=product.get('fallback_id'). While loop with two conditions. Inside: add to visited, append to chain, look up next product, get its fallback_id.",
                "solution": '''def get_fallback_chain(product, product_map):
    chain = []
    visited = set()
    current_id = product.get("fallback_id")

    while current_id is not None and current_id not in visited:
        visited.add(current_id)
        chain.append(current_id)
        fallback_product = product_map.get(current_id)
        if fallback_product is None:
            break
        current_id = fallback_product.get("fallback_id")

    return chain''',
            },
            {
                "title": "Test With Cycles",
                "description": "Create a list of products where product 1->2, 2->3, 3->1 (a cycle). Build the product_map, then call get_fallback_chain for product 1 and verify the result.",
                "hint": "The chain should be [2, 3] because when we get back to 1... wait, let me trace: 2 not visited, add. 3 not visited, add. 1 not visited, add. Then next is 2, which IS visited. Chain = [2, 3, 1].",
                "solution": '''def get_fallback_chain(product, product_map):
    chain = []
    visited = set()
    current_id = product.get("fallback_id")
    while current_id is not None and current_id not in visited:
        visited.add(current_id)
        chain.append(current_id)
        fallback_product = product_map.get(current_id)
        if fallback_product is None:
            break
        current_id = fallback_product.get("fallback_id")
    return chain

products = [
    {"id": 1, "fallback_id": 2},
    {"id": 2, "fallback_id": 3},
    {"id": 3, "fallback_id": 1},  # cycle back to 1
]

product_map = {}
for p in products:
    product_map[p["id"]] = p

chain = get_fallback_chain(products[0], product_map)
print(f"Product 1 chain: {chain}")  # [2, 3, 1]''',
            },
        ],
        "videos": [
            {"title": "DFS Explained Simply", "url": "https://www.youtube.com/watch?v=Urx87-NMm6c"},
        ],
        "interview_tip": "When writing the DFS, say: 'I'm using iterative DFS with a while loop instead of recursion to avoid stack overflow issues, and a visited set to detect cycles.'",
    },
    # ==================== DAY 10 ====================
    {
        "day": 10,
        "phase": 2,
        "title": "Full Solution: All Parts Together",
        "objectives": [
            "Combine retry logic + lookup map + DFS",
            "Write the complete process_products function",
            "Practice the full solution end to end",
        ],
        "concepts": [
            {
                "title": "The Complete Solution",
                "explanation": "Here's everything combined. This is the full answer to the interview. You need to be able to write this clean and fast.",
                "code": '''import time

def retry_api_call(api_function, max_retries=5, sleep_time=2):
    """Part 1: Call API with retry logic."""
    for attempt in range(max_retries):
        try:
            result = api_function()
            return result
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"Attempt {attempt + 1} failed: {e}")
                time.sleep(sleep_time)
            else:
                raise

def get_fallback_chain(product, product_map):
    """Part 2b: Follow fallback chain using iterative DFS."""
    chain = []
    visited = set()
    current_id = product.get("fallback_id")

    while current_id is not None and current_id not in visited:
        visited.add(current_id)
        chain.append(current_id)
        fallback_product = product_map.get(current_id)
        if fallback_product is None:
            break
        current_id = fallback_product.get("fallback_id")

    return chain

def process_products(api_function):
    """Main function: retry API call, then process products."""
    # Part 1: Get products with retry
    products = retry_api_call(api_function)

    # Part 2a: Build lookup map for O(1) access
    product_map = {}
    for product in products:
        product_map[product["id"]] = product

    # Part 2b: Build fallback chains
    for product in products:
        product["related_items"] = get_fallback_chain(
            product, product_map
        )

    return products''',
            },
            {
                "title": "Testing the Full Solution",
                "explanation": "Here's how to test with simulated data:",
                "code": '''import time
import random

# Simulate a flaky API server
call_count = [0]

def fake_api():
    call_count[0] += 1
    # 67% failure rate
    if random.random() < 0.67:
        raise Exception(f"Server Error (call #{call_count[0]})")
    # Return product data
    return [
        {"id": 1, "fallback_id": 2},
        {"id": 2, "fallback_id": 3},
        {"id": 3, "fallback_id": None},
        {"id": 4, "fallback_id": 5},
        {"id": 5, "fallback_id": 4},  # cycle with 4!
    ]

# Run the full solution (using 0.1s sleep for faster testing)
def retry_api_call(api_fn, max_retries=5, sleep_time=0.1):
    for attempt in range(max_retries):
        try:
            return api_fn()
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"Attempt {attempt+1} failed: {e}")
                time.sleep(sleep_time)
            else:
                raise

def get_fallback_chain(product, product_map):
    chain = []
    visited = set()
    current_id = product.get("fallback_id")
    while current_id is not None and current_id not in visited:
        visited.add(current_id)
        chain.append(current_id)
        fp = product_map.get(current_id)
        if fp is None:
            break
        current_id = fp.get("fallback_id")
    return chain

# Run it
products = retry_api_call(fake_api)
product_map = {p["id"]: p for p in products}
for p in products:
    p["related_items"] = get_fallback_chain(p, product_map)
    print(f"Product {p['id']}: related = {p['related_items']}")''',
            },
        ],
        "exercises": [
            {
                "title": "Write the Full Solution From Memory",
                "description": "Write ALL THREE functions (retry_api_call, get_fallback_chain, process_products) from memory. This should take under 10 minutes.",
                "hint": "Start with imports. Then retry function. Then DFS function. Then the main process_products that calls both.",
                "solution": '''import time

def retry_api_call(api_function, max_retries=5, sleep_time=2):
    for attempt in range(max_retries):
        try:
            result = api_function()
            return result
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"Attempt {attempt + 1} failed: {e}")
                time.sleep(sleep_time)
            else:
                raise

def get_fallback_chain(product, product_map):
    chain = []
    visited = set()
    current_id = product.get("fallback_id")
    while current_id is not None and current_id not in visited:
        visited.add(current_id)
        chain.append(current_id)
        fallback_product = product_map.get(current_id)
        if fallback_product is None:
            break
        current_id = fallback_product.get("fallback_id")
    return chain

def process_products(api_function):
    products = retry_api_call(api_function)

    product_map = {}
    for product in products:
        product_map[product["id"]] = product

    for product in products:
        product["related_items"] = get_fallback_chain(product, product_map)

    return products''',
            },
        ],
        "videos": [],
        "interview_tip": "In the interview, write Part 1 first and TEST it before moving to Part 2. Don't try to write everything at once. Show incremental progress.",
    },
    # ==================== DAY 11 ====================
    {
        "day": 11,
        "phase": 2,
        "title": "Connected Components (Stretch Goal)",
        "objectives": [
            "Understand the connected components concept",
            "Implement shared related_items lists",
            "Know when to stop optimizing",
        ],
        "concepts": [
            {
                "title": "Connected Components",
                "explanation": "If product 1's chain includes products 2 and 3, then they're all 'connected.' In Part 3, ALL connected products should share the same related_items (minus themselves). Alex said not to over-index on this, but understand the concept.",
                "code": '''# Before connected components:
# Product 1: related_items = [2, 3]
# Product 2: related_items = [3]
# Product 3: related_items = []

# After connected components:
# Product 1: related_items = [2, 3]  (same)
# Product 2: related_items = [1, 3]  (added 1!)
# Product 3: related_items = [1, 2]  (added 1, 2!)

# The idea: if A connects to B, then B connects to A
# They're in the same "component"

def build_connected_components(products, product_map):
    # First, build fallback chains as before
    for product in products:
        product["related_items"] = get_fallback_chain(
            product, product_map
        )

    # Then, for each product, add it to its related products' lists
    for product in products:
        pid = product["id"]
        for related_id in product["related_items"]:
            related = product_map.get(related_id)
            if related is not None:
                if "related_items" not in related:
                    related["related_items"] = []
                if pid not in related["related_items"]:
                    related["related_items"].append(pid)''',
            },
            {
                "title": "Union-Find Approach (Advanced)",
                "explanation": "A more elegant approach uses Union-Find to group connected products. This is the 'proper' CS approach but may be overkill for the interview.",
                "code": '''# Union-Find groups elements into sets
# When two products are connected, union their groups
# At the end, all products in the same group share related_items

# Simple approach: just use sets
def find_components(products, product_map):
    components = {}  # product_id -> set of connected ids

    for product in products:
        pid = product["id"]
        chain = get_fallback_chain(product, product_map)

        # All products in this chain are connected
        connected = set([pid] + chain)

        # Merge with existing components
        merged = set()
        for cid in connected:
            if cid in components:
                merged.update(components[cid])
        merged.update(connected)

        # Update all products in the component
        for cid in merged:
            components[cid] = merged

    # Set related_items (exclude self)
    for product in products:
        pid = product["id"]
        if pid in components:
            product["related_items"] = [
                x for x in components[pid] if x != pid
            ]

    return products

# Don't stress about Part 3. Focus on nailing Parts 1 and 2.''',
            },
        ],
        "exercises": [
            {
                "title": "Trace Connected Components",
                "description": "Given products: 1->2, 2->3, 3->None, 4->5, 5->None. List the connected components (groups of products that are related).",
                "hint": "Product 1 connects to 2 connects to 3. Product 4 connects to 5. These are two separate groups.",
                "solution": '''# Component 1: {1, 2, 3}
#   Product 1 related: [2, 3]
#   Product 2 related: [1, 3]
#   Product 3 related: [1, 2]

# Component 2: {4, 5}
#   Product 4 related: [5]
#   Product 5 related: [4]

# Each product's related_items includes all other
# products in its component, but NOT itself.''',
            },
        ],
        "videos": [
            {"title": "Connected Components in Graphs", "url": "https://www.youtube.com/watch?v=8aHj9bPeHlM"},
        ],
        "interview_tip": "If you get to Part 3, say: 'I'd approach connected components by tracking which products are reachable from each other and creating shared related_items lists.' Even describing the approach earns points.",
    },
    # ==================== DAY 12 ====================
    {
        "day": 12,
        "phase": 2,
        "title": "Practice Problems",
        "objectives": [
            "Solve Two Sum (dictionary lookup pattern)",
            "Detect a cycle (visited set pattern)",
            "Practice explaining your approach out loud",
        ],
        "concepts": [
            {
                "title": "Two Sum (Classic Dictionary Problem)",
                "explanation": "Two Sum uses the EXACT same pattern as building a lookup map. You create a dictionary for O(1) lookup. This reinforces the interview skill.",
                "code": '''# Two Sum: find two numbers that add up to target
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1] (because nums[0] + nums[1] = 9)

def two_sum(nums, target):
    seen = {}  # value -> index (lookup map!)

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []  # no solution found

# The pattern is the same as the interview:
# Build a dictionary for O(1) lookup
# Instead of searching the list each time

print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
print(two_sum([3, 2, 4], 6))        # [1, 2]''',
            },
            {
                "title": "Linked List Cycle Detection",
                "explanation": "This is exactly the visited set pattern from the interview. Follow links, track visited nodes, detect when you revisit.",
                "code": '''# Simulate a linked list with a dictionary
# Each node points to the next node
nodes = {
    "A": "B",
    "B": "C",
    "C": "D",
    "D": "B",  # Points back to B = cycle!
}

def has_cycle(start, nodes):
    visited = set()
    current = start

    while current is not None and current not in visited:
        visited.add(current)
        current = nodes.get(current)

    return current is not None  # True if we hit a visited node

print(has_cycle("A", nodes))  # True (D -> B creates cycle)

# No cycle version:
nodes2 = {"A": "B", "B": "C", "C": None}
print(has_cycle("A", nodes2))  # False''',
            },
        ],
        "exercises": [
            {
                "title": "Two Sum",
                "description": "Write the two_sum function from scratch. Given a list of numbers and a target, return the indices of two numbers that add up to the target. Use a dictionary for O(1) lookup.",
                "hint": "For each number, calculate what complement you need (target - num). Check if complement is in your seen dictionary.",
                "solution": '''def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

print(two_sum([2, 7, 11, 15], 9))  # [0, 1]''',
            },
            {
                "title": "Find Chain Length",
                "description": "Write a function that takes a start_id and a chain_map (dict mapping id to next id) and returns the length of the chain before hitting None or a cycle.",
                "hint": "Use the while loop + visited set pattern. Count how many nodes you visit.",
                "solution": '''def chain_length(start_id, chain_map):
    visited = set()
    current = start_id
    length = 0

    while current is not None and current not in visited:
        visited.add(current)
        length += 1
        current = chain_map.get(current)

    return length

chain_map = {1: 2, 2: 3, 3: 4, 4: None}
print(chain_length(1, chain_map))  # 4

cycle_map = {1: 2, 2: 3, 3: 1}
print(chain_length(1, cycle_map))  # 3''',
            },
        ],
        "videos": [
            {"title": "Two Sum - LeetCode (NeetCode)", "url": "https://www.youtube.com/watch?v=KLlXCFG5TnA"},
        ],
        "interview_tip": "These problems use the SAME patterns as your interview: dictionary lookups, visited sets, and while-loop traversal. The concepts transfer directly.",
    },
    # ==================== DAY 13 ====================
    {
        "day": 13,
        "phase": 2,
        "title": "Debugging Practice",
        "objectives": [
            "Read code line by line and track variable values",
            "Find bugs by tracing execution",
            "Practice systematic debugging",
        ],
        "concepts": [
            {
                "title": "Debugging by Tracing",
                "explanation": "The debugging round tests whether you can read code carefully and track what happens at each step. The trick: go line by line, write down every variable's value after each line executes. Use Cmd+F to find things in the codebase.",
                "code": '''# TRACE THROUGH THIS CODE - what does it print?

x = 5
y = 3
result = []

for i in range(y):
    if x > 3:
        result.append(i * 2)
        x -= 1
    else:
        result.append(i)

print(result)

# TRACE:
# i=0: x=5 > 3? Yes. append 0*2=0. x=4. result=[0]
# i=1: x=4 > 3? Yes. append 1*2=2. x=3. result=[0, 2]
# i=2: x=3 > 3? No.  append 2.     x=3. result=[0, 2, 2]
# Answer: [0, 2, 2]''',
            },
            {
                "title": "Finding Bugs",
                "explanation": "Common bugs to look for: off-by-one errors, wrong variable names, missing .get() causing KeyError, forgetting to update a variable, wrong comparison operator.",
                "code": '''# BUG 1: Off-by-one error
# This retries max_retries+1 times instead of max_retries
def retry_bad(func, max_retries=5):
    for attempt in range(max_retries + 1):  # BUG: should be range(max_retries)
        try:
            return func()
        except:
            pass

# BUG 2: Not updating current_id
def follow_chain_bad(product, product_map):
    chain = []
    current_id = product.get("fallback_id")
    visited = set()
    while current_id is not None and current_id not in visited:
        visited.add(current_id)
        chain.append(current_id)
        # BUG: forgot to update current_id!
        # current_id = product_map.get(current_id, {}).get("fallback_id")
    return chain  # This either loops forever or returns wrong result

# BUG 3: Using [] instead of .get()
def process_bad(products):
    product_map = {}
    for p in products:
        product_map[p["id"]] = p
    # BUG: product_map[99] crashes if 99 not in map
    # FIX: product_map.get(99)''',
            },
        ],
        "exercises": [
            {
                "title": "Trace This Code",
                "description": "Trace through this code by hand and predict the output:\n\ndata = {'a': 1, 'b': 2, 'c': 3}\nresult = []\nfor key, val in data.items():\n    if val > 1:\n        result.append(key)\nprint(result)",
                "hint": "Go through each key-value pair: a:1 (skip), b:2 (append), c:3 (append).",
                "solution": '''# Trace:
# key='a', val=1: 1 > 1? No. Skip.
# key='b', val=2: 2 > 1? Yes. result=['b']
# key='c', val=3: 3 > 1? Yes. result=['b', 'c']
# Output: ['b', 'c']

data = {"a": 1, "b": 2, "c": 3}
result = []
for key, val in data.items():
    if val > 1:
        result.append(key)
print(result)  # ['b', 'c']''',
            },
            {
                "title": "Find the Bug",
                "description": "This function is supposed to build a lookup map but has a bug. Find and fix it:\n\ndef build_map(products):\n    product_map = {}\n    for product in products:\n        product_map[product['name']] = product\n    return product_map",
                "hint": "The map should use product ID as the key (for O(1) lookup by ID), not the product name.",
                "solution": '''# BUG: Uses product['name'] as key instead of product['id']
# This means you can't look up products by ID!

# FIXED:
def build_map(products):
    product_map = {}
    for product in products:
        product_map[product["id"]] = product  # Fixed: use 'id' as key
    return product_map''',
            },
        ],
        "videos": [
            {"title": "Python Debugging Tips (Corey Schafer)", "url": "https://www.youtube.com/watch?v=ChuU3NlYRLQ"},
        ],
        "interview_tip": "In the debugging round, use Cmd+F to search the codebase. Read line by line. Write down variable values. Don't skip steps.",
    },
    # ==================== DAY 14 ====================
    {
        "day": 14,
        "phase": 2,
        "title": "Phase 2 Checkpoint - Full Timed Run",
        "objectives": [
            "Complete the full interview problem in under 45 minutes",
            "Practice talking through your solution",
            "Identify areas that need more speed",
        ],
        "concepts": [
            {
                "title": "Timed Practice Instructions",
                "explanation": "Set a 45-minute timer. Write the complete solution from scratch as if you were in the interview. Talk out loud the entire time. Include: retry logic, lookup map, DFS fallback chains. Don't look at notes!",
                "code": '''# YOUR GOAL: Write all of this in 45 minutes
# Start your timer NOW

# Step 1 (target: 8 minutes): Write retry_api_call
# - import time
# - for loop with max_retries
# - try/except with absorb/throw
# - time.sleep between retries

# Step 2 (target: 3 minutes): Build lookup map
# - Loop through products
# - Map product_id -> product dict

# Step 3 (target: 12 minutes): Write get_fallback_chain
# - Initialize chain list and visited set
# - While loop with two conditions
# - Look up products in map with .get()
# - Handle None and cycles

# Step 4 (target: 5 minutes): Write process_products
# - Call retry_api_call
# - Build map
# - Loop through products and set related_items

# Step 5 (target: 5 minutes): Test and trace through
# - Create test data
# - Trace through by hand
# - Verify edge cases

# Remaining time: Polish and handle Part 3 if time allows''',
            },
        ],
        "exercises": [
            {
                "title": "Full Timed Solution",
                "description": "Write the COMPLETE solution: retry_api_call, get_fallback_chain, and process_products. Time yourself. Target: under 30 minutes for the code, 15 minutes for testing/tracing.",
                "hint": "Don't peek! If you can't do it in 45 minutes, that's okay - identify what slowed you down and practice that part tomorrow.",
                "solution": '''import time

def retry_api_call(api_function, max_retries=5, sleep_time=2):
    for attempt in range(max_retries):
        try:
            result = api_function()
            return result
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"Attempt {attempt + 1} failed: {e}")
                time.sleep(sleep_time)
            else:
                raise

def get_fallback_chain(product, product_map):
    chain = []
    visited = set()
    current_id = product.get("fallback_id")
    while current_id is not None and current_id not in visited:
        visited.add(current_id)
        chain.append(current_id)
        fallback_product = product_map.get(current_id)
        if fallback_product is None:
            break
        current_id = fallback_product.get("fallback_id")
    return chain

def process_products(api_function):
    products = retry_api_call(api_function)

    product_map = {}
    for product in products:
        product_map[product["id"]] = product

    for product in products:
        product["related_items"] = get_fallback_chain(product, product_map)

    return products

# Test with sample data
def fake_api():
    return [
        {"id": 1, "fallback_id": 2},
        {"id": 2, "fallback_id": 3},
        {"id": 3, "fallback_id": None},
        {"id": 4, "fallback_id": 5},
        {"id": 5, "fallback_id": 4},
    ]

products = process_products(fake_api)
for p in products:
    print(f"Product {p['id']}: related = {p['related_items']}")''',
            },
        ],
        "videos": [],
        "interview_tip": "Time check: Part 1 should take no more than 10 minutes. If it takes longer, you need more practice on Days 5-6. The bulk of your time should be on Part 2.",
    },
    # ==================== DAY 15 ====================
    {
        "day": 15,
        "phase": 3,
        "title": "Mock Interview: Solo Run",
        "objectives": [
            "Simulate the full interview experience",
            "Practice explaining your thinking out loud",
            "Build confidence with the complete flow",
        ],
        "concepts": [
            {
                "title": "Solo Mock Interview Guide",
                "explanation": "Pretend you're in the real interview. Set up your environment, start a timer, and talk out loud as if an engineer is watching you. Record yourself if possible to review later.",
                "code": '''# MOCK INTERVIEW SCRIPT
# Total time: 60 minutes

# MINUTE 0-3: Read the problem
# "Let me read through the server code to understand
#  the error patterns..."
# "I see two types of errors: 429 rate limiting and
#  random server errors with 67% failure rate"

# MINUTE 3-5: Plan your approach (out loud!)
# "My plan is:
#  1. Write retry logic with 5 retries and 2-second sleep
#  2. Build a hashmap from product ID to product
#  3. Use iterative DFS to follow fallback chains
#  4. Handle edge cases: None, cycles, missing products"

# MINUTE 5-15: Write Part 1 (retry logic)
# Write it, test it, move on FAST

# MINUTE 15-20: Build lookup map
# "I'm building a hashmap for O(1) lookup"

# MINUTE 20-40: Write DFS + test it
# This is where you spend the most time
# Test with normal chain, cycle, and None cases

# MINUTE 40-50: Polish + Part 3 if time allows
# "If I had more time, I'd implement connected components
#  by tracking bidirectional relationships"

# MINUTE 50-60: Final review and questions
# "Let me trace through one more example to verify..."''',
            },
            {
                "title": "What to Say Out Loud",
                "explanation": "Practice these phrases until they feel natural:",
                "code": '''# THINGS TO SAY IN THE INTERVIEW:

# When starting:
# "Let me read through the code first before jumping in"

# When writing retry logic:
# "I'll retry 5 times because (2/3)^5 gives about 13%
#  chance all five fail, so roughly 87% success rate"
# "I'm sleeping 2 seconds because the server rate limits
#  within a random window up to 2 seconds"

# When building the map:
# "I'm building a hashmap from product ID to product
#  for O(1) lookup instead of searching the list"

# When writing DFS:
# "I'm using iterative DFS with a while loop and a
#  visited set to detect cycles"
# "I'm using .get() for safe dictionary access in case
#  a product references an ID not in our data"

# When testing:
# "Let me trace through this with a quick example"

# When stuck:
# "Let me think about this for a second"

# If running out of time:
# "This is what I would have done next..."''',
            },
        ],
        "exercises": [
            {
                "title": "60-Minute Mock Interview",
                "description": "Set a 60-minute timer. Open a blank file. Write the complete solution from scratch while talking out loud. Pretend someone is watching. When done, review: How long did each part take? Where did you hesitate? What would you say differently?",
                "hint": "Part 1 target: 10 min. Lookup map: 5 min. DFS: 15 min. Testing: 10 min. That leaves 20 min for polish and Part 3.",
                "solution": '''# There's no single "solution" here - the goal is practice.
# Review checklist:
# [ ] Did Part 1 take under 10 minutes?
# [ ] Did you explain the math (87% success rate)?
# [ ] Did you explain the 2-second sleep?
# [ ] Did you mention O(1) lookup for the hashmap?
# [ ] Did you mention the visited set for cycle detection?
# [ ] Did you handle None fallback_id?
# [ ] Did you handle cycles?
# [ ] Did you trace through an example?
# [ ] Did you talk continuously?''',
            },
        ],
        "videos": [],
        "interview_tip": "The biggest mistake is going silent. Even when you're thinking, say 'Let me think about this for a moment' rather than sitting in silence. The interviewer wants to hear your thought process.",
    },
    # ==================== DAY 16 ====================
    {
        "day": 16,
        "phase": 3,
        "title": "Speed Drills",
        "objectives": [
            "Write each function as fast as possible",
            "Identify and eliminate hesitation points",
            "Build muscle memory",
        ],
        "concepts": [
            {
                "title": "Speed Drill Instructions",
                "explanation": "Do each drill 3 times. Time yourself each time. Your goal is to get faster with each attempt. Rest 2 minutes between attempts.",
                "code": '''# DRILL 1: Retry Function (target: 3 minutes)
# Write retry_api_call from memory
# Time yourself. Do it 3 times.

# DRILL 2: Lookup Map (target: 1 minute)
# Given a list of products, build the product_map
# This should be INSTANT - no thinking required

# DRILL 3: DFS Function (target: 5 minutes)
# Write get_fallback_chain from memory
# Time yourself. Do it 3 times.

# DRILL 4: Full Solution (target: 12 minutes)
# All three functions together
# Time yourself. Do it 3 times.

# Track your times:
# Attempt 1: ___ minutes
# Attempt 2: ___ minutes
# Attempt 3: ___ minutes''',
            },
        ],
        "exercises": [
            {
                "title": "Drill: Retry Function (3 min target)",
                "description": "Write retry_api_call as fast as you can. Time yourself. Include import time, default parameters, for loop, try/except, absorb/throw, time.sleep.",
                "hint": "Just start typing. Don't think too hard. Your fingers should know the pattern by now.",
                "solution": '''import time

def retry_api_call(api_function, max_retries=5, sleep_time=2):
    for attempt in range(max_retries):
        try:
            result = api_function()
            return result
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"Attempt {attempt + 1} failed: {e}")
                time.sleep(sleep_time)
            else:
                raise''',
            },
            {
                "title": "Drill: DFS Function (5 min target)",
                "description": "Write get_fallback_chain as fast as you can. Time yourself.",
                "hint": "chain=[], visited=set(), get fallback_id, while loop, add/append, lookup, get next fallback_id.",
                "solution": '''def get_fallback_chain(product, product_map):
    chain = []
    visited = set()
    current_id = product.get("fallback_id")
    while current_id is not None and current_id not in visited:
        visited.add(current_id)
        chain.append(current_id)
        fallback_product = product_map.get(current_id)
        if fallback_product is None:
            break
        current_id = fallback_product.get("fallback_id")
    return chain''',
            },
        ],
        "videos": [],
        "interview_tip": "Speed comes from repetition, not rushing. If you've practiced enough, the code flows naturally. If you're still hesitating, go back and practice the specific part you're slow on.",
    },
    # ==================== DAY 17 ====================
    {
        "day": 17,
        "phase": 3,
        "title": "Mock Interview with a Friend",
        "objectives": [
            "Practice with another person watching",
            "Get feedback on communication style",
            "Practice handling questions and interruptions",
        ],
        "concepts": [
            {
                "title": "Instructions for Your Mock Interviewer",
                "explanation": "Send these instructions to whoever is helping you practice. They don't need to know how to code - they just need to watch and give feedback.",
                "code": '''# FOR YOUR MOCK INTERVIEWER:
#
# 1. Set a 60-minute timer
#
# 2. Give Lindsay this prompt:
#    "You're given an unreliable API server. You can't
#    modify the server. Write client code that handles
#    the server's unreliability and processes the data."
#
# 3. Watch for these things:
#    - Does she explain her approach before coding?
#    - Does she talk through what she's doing?
#    - Does she stay calm when something doesn't work?
#    - Does she test her code?
#    - Does she explain WHY she makes decisions?
#
# 4. Ask these questions during the interview:
#    - "Why did you choose 5 retries?"
#    - "What happens if there's a cycle?"
#    - "What's the time complexity of your lookup?"
#    - "How would you handle a new type of error?"
#
# 5. After the interview, give feedback on:
#    - Communication clarity
#    - Code organization
#    - Problem-solving approach
#    - Confidence level''',
            },
        ],
        "exercises": [
            {
                "title": "Post-Mock Review",
                "description": "After your mock interview, answer these questions:\n1. What went well?\n2. Where did you hesitate or go silent?\n3. What questions were hard to answer?\n4. What would you do differently?\n5. Rate your confidence 1-10.",
                "hint": "Be honest with yourself. The goal is improvement, not perfection.",
                "solution": '''# This is a self-reflection exercise.
# Write your answers down somewhere you can review them.
#
# Common issues to work on:
# - Going silent -> practice talking through your thinking
# - Slow Part 1 -> do more speed drills
# - Forgetting edge cases -> review Day 9
# - Not testing -> always trace through an example
# - Not explaining WHY -> practice the phrases from Day 15''',
            },
        ],
        "videos": [],
        "interview_tip": "Having another person watch you changes everything. The nervousness is normal. The more you practice with an audience, the more comfortable you'll be on interview day.",
    },
    # ==================== DAY 18 ====================
    {
        "day": 18,
        "phase": 3,
        "title": "Debugging Deep Dive",
        "objectives": [
            "Practice systematic code tracing",
            "Find bugs in complex code",
            "Build confidence for the debugging round",
        ],
        "concepts": [
            {
                "title": "Systematic Debugging Process",
                "explanation": "For the debugging round, follow this exact process: (1) Read the code top to bottom, (2) Identify inputs, (3) Trace each line, writing down variable values, (4) Find where actual behavior differs from expected.",
                "code": '''# PRACTICE: Trace this code step by step

def mystery(items):
    result = {}
    for item in items:
        key = item["type"]
        if key not in result:
            result[key] = []
        result[key].append(item["name"])
    return result

data = [
    {"name": "Alice", "type": "admin"},
    {"name": "Bob", "type": "user"},
    {"name": "Charlie", "type": "admin"},
    {"name": "Diana", "type": "user"},
]

output = mystery(data)
print(output)

# TRACE:
# item = {"name": "Alice", "type": "admin"}
#   key = "admin", not in result -> result = {"admin": []}
#   append -> result = {"admin": ["Alice"]}
#
# item = {"name": "Bob", "type": "user"}
#   key = "user", not in result -> result = {"admin": ["Alice"], "user": []}
#   append -> result = {"admin": ["Alice"], "user": ["Bob"]}
#
# item = {"name": "Charlie", "type": "admin"}
#   key = "admin", IS in result (skip if)
#   append -> result = {"admin": ["Alice", "Charlie"], "user": ["Bob"]}
#
# item = {"name": "Diana", "type": "user"}
#   key = "user", IS in result (skip if)
#   append -> result = {"admin": ["Alice", "Charlie"], "user": ["Bob", "Diana"]}
#
# Output: {"admin": ["Alice", "Charlie"], "user": ["Bob", "Diana"]}''',
            },
        ],
        "exercises": [
            {
                "title": "Trace Complex Code",
                "description": "Trace through this code and predict the output:\n\ndef process(data, threshold):\n    above = []\n    below = []\n    for item in data:\n        if item > threshold:\n            above.append(item)\n        elif item < threshold:\n            below.append(item)\n    return {'above': above, 'below': below, 'equal': len(data) - len(above) - len(below)}\n\nresult = process([3, 7, 5, 2, 5, 8, 1], 5)\nprint(result)",
                "hint": "Go through each number: 3<5, 7>5, 5==5 (neither), 2<5, 5==5, 8>5, 1<5.",
                "solution": '''# Trace: threshold = 5
# 3: 3 > 5? No. 3 < 5? Yes. below = [3]
# 7: 7 > 5? Yes. above = [7]
# 5: 5 > 5? No. 5 < 5? No. (equal)
# 2: 2 < 5? Yes. below = [3, 2]
# 5: same as above (equal)
# 8: 8 > 5? Yes. above = [7, 8]
# 1: 1 < 5? Yes. below = [3, 2, 1]
#
# equal = 7 - 2 - 3 = 2
# Output: {'above': [7, 8], 'below': [3, 2, 1], 'equal': 2}''',
            },
            {
                "title": "Find the Bug",
                "description": "This DFS function has a bug that causes it to miss some items in the chain. Find and fix it:\n\ndef get_chain(start_id, graph):\n    chain = []\n    visited = set()\n    current = start_id\n    while current is not None:\n        if current in visited:\n            break\n        chain.append(current)\n        current = graph.get(current)\n    return chain",
                "hint": "The visited set is created but never gets items added to it. Without adding to visited, cycle detection doesn't work.",
                "solution": '''# BUG: visited.add(current) is missing!
# The visited set is never populated, so cycle detection
# doesn't work. The while loop would run forever on cycles.

def get_chain(start_id, graph):
    chain = []
    visited = set()
    current = start_id
    while current is not None:
        if current in visited:
            break
        visited.add(current)  # FIX: add this line!
        chain.append(current)
        current = graph.get(current)
    return chain

# Test with a cycle
graph = {1: 2, 2: 3, 3: 1}
print(get_chain(1, graph))  # [1, 2, 3]''',
            },
        ],
        "videos": [],
        "interview_tip": "In the debugging round, don't guess. Trace EVERY line. Write down variable values. The bugs are always subtle - a missing line, a wrong variable, an off-by-one error.",
    },
    # ==================== DAY 19 ====================
    {
        "day": 19,
        "phase": 3,
        "title": "Final Full Simulation",
        "objectives": [
            "One last full practice run",
            "Nail the timing",
            "Polish your verbal explanations",
        ],
        "concepts": [
            {
                "title": "Final Simulation Checklist",
                "explanation": "This is your dress rehearsal. Do everything exactly as you would in the real interview. Close all notes. Open a blank editor. Set a 60-minute timer. Talk out loud.",
                "code": '''# PRE-INTERVIEW CHECKLIST:
# [ ] Blank editor open
# [ ] Timer set for 60 minutes
# [ ] Notes CLOSED
# [ ] Ready to talk out loud

# DURING THE INTERVIEW:
# [ ] Read the problem carefully (2-3 min)
# [ ] State your plan before coding
# [ ] Write Part 1 (retry) - target 8 min
# [ ] Test Part 1
# [ ] Build lookup map - target 3 min
# [ ] Write Part 2 (DFS) - target 12 min
# [ ] Test with normal chain
# [ ] Test with cycle
# [ ] Test with None fallback
# [ ] Write process_products tying it together - 5 min
# [ ] Trace through a complete example

# KEY PHRASES TO USE:
# "87% success rate with 5 retries"
# "2-second sleep clears the rate limit window"
# "O(1) lookup with the hashmap"
# "Visited set for cycle detection"
# "Let me trace through this example"

# IF NOT FINISHED:
# "This is what I would have done next..."''',
            },
        ],
        "exercises": [
            {
                "title": "Final Full Run",
                "description": "Complete the full interview simulation one more time. This is your LAST practice. Make it count. After you're done, note your total time and any remaining hesitation points.",
                "hint": "You've done this many times now. Trust your practice. The code should flow naturally.",
                "solution": '''import time

def retry_api_call(api_function, max_retries=5, sleep_time=2):
    for attempt in range(max_retries):
        try:
            result = api_function()
            return result
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"Attempt {attempt + 1} failed: {e}")
                time.sleep(sleep_time)
            else:
                raise

def get_fallback_chain(product, product_map):
    chain = []
    visited = set()
    current_id = product.get("fallback_id")
    while current_id is not None and current_id not in visited:
        visited.add(current_id)
        chain.append(current_id)
        fallback_product = product_map.get(current_id)
        if fallback_product is None:
            break
        current_id = fallback_product.get("fallback_id")
    return chain

def process_products(api_function):
    products = retry_api_call(api_function)

    product_map = {}
    for product in products:
        product_map[product["id"]] = product

    for product in products:
        product["related_items"] = get_fallback_chain(product, product_map)

    return products''',
            },
        ],
        "videos": [],
        "interview_tip": "You're ready. Trust your preparation. The most important thing tomorrow is to stay calm and communicate clearly.",
    },
    # ==================== DAY 20 ====================
    {
        "day": 20,
        "phase": 3,
        "title": "Rest & Final Prep",
        "objectives": [
            "Light review only - do NOT cram",
            "Prepare mentally and logistically",
            "Confidence building",
        ],
        "concepts": [
            {
                "title": "The Day Before",
                "explanation": "Today is about REST, not cramming. A quick review, logistics check, and mental preparation. You've put in the work. Trust it.",
                "code": '''# QUICK REVIEW (15 minutes max):
# Just read through the solution one more time.
# Don't try to memorize - let your practice carry you.

# KEY POINTS TO REMEMBER:
# 1. Read the problem before coding
# 2. State your plan out loud
# 3. Write Part 1 fast, test it, move on
# 4. Build the hashmap, explain O(1)
# 5. Write DFS with visited set
# 6. Test with examples
# 7. Handle edge cases (None, cycles)
# 8. Talk through EVERYTHING

# LOGISTICS:
# [ ] Interview link/location confirmed
# [ ] Computer charged
# [ ] Editor ready
# [ ] Water nearby
# [ ] Quiet environment

# MENTAL PREP:
# - You've practiced this problem dozens of times
# - You know the exact patterns they're testing
# - You have inside intel on what to expect
# - You can explain WHY for every decision
# - If you don't finish: "this is what I would've done"''',
            },
            {
                "title": "Confidence Reminders",
                "explanation": "Read these reminders before the interview:",
                "code": '''# YOU HAVE ADVANTAGES MOST CANDIDATES DON'T:

# 1. You know the exact interview format
#    (most people go in blind)

# 2. You know the specific error types
#    (429 rate limiting + 67% random failure)

# 3. You know the exact solution pattern
#    (retry + hashmap + iterative DFS)

# 4. You know what to say out loud
#    (87% success rate, O(1) lookup, visited set)

# 5. You've practiced the full problem many times
#    (most candidates see it for the first time)

# 6. You bring unique AI/product perspective
#    (trust & safety, responsible AI, product thinking)

# The coding is ONE part of the interview.
# Your product sense, communication, and thinking
# are also being evaluated. You're strong there.

# GO GET IT, LINDSAY! 🎯''',
            },
        ],
        "exercises": [
            {
                "title": "Quick Confidence Check",
                "description": "Without writing code, verbally answer these questions as if the interviewer asked them:\n1. Why 5 retries?\n2. Why 2-second sleep?\n3. Why build a hashmap?\n4. How do you handle cycles?\n5. What's your overall approach?",
                "hint": "Say the answers out loud. Practice until they sound natural, not rehearsed.",
                "solution": '''# Verbal answers:

# 1. "5 retries because with a 67% failure rate,
#     (2/3)^5 gives about 13% chance all five fail,
#     so roughly 87% success rate."

# 2. "2-second sleep because the server rate limits
#     within a random window up to 2 seconds.
#     Sleeping 2 seconds guarantees we clear it."

# 3. "I build a hashmap from product ID to product
#     for O(1) lookup instead of searching the list
#     each time I need to find a product."

# 4. "I use a visited set. Before processing each
#     product in the chain, I check if it's in the set.
#     If it is, that's a cycle and I stop."

# 5. "My approach: First, write retry logic to handle
#     the unreliable API. Then build a lookup map from
#     the product data. Then use iterative DFS with a
#     visited set to follow each product's fallback chain."''',
            },
        ],
        "videos": [],
        "interview_tip": "Get good sleep tonight. You've done the work. Tomorrow, just be yourself and show them what you know.",
    },
]
