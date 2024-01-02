from gpt4all import GPT4All


if __name__ == '__main__':

    model = GPT4All("mistral-7b-instruct-v0.1.Q4_0.gguf")
    output = model.generate("Answer this prompt by saying ‘Hello LLM'", max_tokens=1000)
    print("Instruct: ")
    print(output)
    model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")
    output = model.generate("Answer this prompt by saying ‘Hello LLM'", max_tokens=1000)
    print("openorca: ")
    print(output)