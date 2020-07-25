from textgenrnn import textgenrnn

textgen = textgenrnn()

textgen.train_from_file('input.txt', num_epochs=200)
print("=" * 20)
textgen.generate(5)