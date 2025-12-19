from transformers import AutoTokenizer, AutoModelForCausalLM

tok = AutoTokenizer.from_pretrained("out")
model = AutoModelForCausalLM.from_pretrained("out")

while True:
    q = input("> ")
    x = tok(q, return_tensors="pt")
    y = model.generate(**x, max_new_tokens=40)
    print(tok.decode(y[0], skip_special_tokens=True))
