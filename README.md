# hill-cipher-bruteforce
Quick python script to brutforce all 2x2 matrices in a hill cipher (originally made as an attempt in a ctf)

## Usage
Change input string in hill() to the string you want to bruteforce decode. Useful to check against a dictionary for possible answers. Technically you can try higher order matrices by changing n,m and blocksize, but the complexity increases very quickly (26^n^2)
