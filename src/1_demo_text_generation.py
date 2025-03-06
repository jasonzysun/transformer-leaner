from transformers import logging, pipeline

logging.set_verbosity_info()
generator = pipeline('text-generation', model='gpt2', device=0)
prompt = "Hello, I'm learning about transformers!"
results = generator(prompt)
print(results)