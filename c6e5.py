str = 'X-DSPAM-Confidence:0.8475'

position = str.find(':')

number = str[position+1:]

conv_number = float(number)

print(conv_number)
