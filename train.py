from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments
from datasets import load_dataset

MODEL = "skt/kogpt2-base-v2"

tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForCausalLM.from_pretrained(MODEL)

ds = load_dataset("text", data_files="data.txt")

def tok(x):
    return tokenizer(x["text"], truncation=True, max_length=128)

ds = ds.map(tok, batched=True, remove_columns=["text"])

args = TrainingArguments(
    output_dir="out",
    num_train_epochs=1,
    per_device_train_batch_size=2,
    logging_steps=20,
    save_steps=500,
    report_to="none"
)

Trainer(model=model, args=args, train_dataset=ds["train"]).train()

model.save_pretrained("out")
tokenizer.save_pretrained("out")
