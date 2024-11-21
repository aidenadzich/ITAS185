from openai import OpenAI

client = OpenAI()


input_animal = input("Enter an animal: ")
input_body = input("Enter a body part: ")
input_setting = input("Enter a location and a year: ")

completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
                {"role": "system", "content": "You are a author that specializes in writing childrens stories (suitable for 5 year olds) of at least 300 words that is based on 3 items received by 3 seperate prompts from the user. They have to be a animal, a body part, and a location + year, and they must be in that order. If you don't get all of those 3, don't write a story and tell the user to restart the program. Do the same thing if 2 of the same category are entered. Absolutely do not start writing the story until you receive all 3 categories."},
                {"role": "user", "content": input_animal + input_body + input_setting}
            ]
    )

print(f'AI Author: {completion.choices[0].message.content}')