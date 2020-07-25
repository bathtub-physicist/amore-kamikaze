from textgenrnn import textgenrnn

textgen = textgenrnn('textgenrnn_weights.hdf5')
textgen.generate_to_file('output.txt', n=50, temperature=1)