import colorama
import transformations

def main():
    colorama.init()
    transformations.ToClip(transformations.select_file())
    
main()
