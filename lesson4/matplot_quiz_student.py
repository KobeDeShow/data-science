import pandas as pd
import matplotlib.pyplot as plt


def lineplot(hr_year_csv):
    data = pd.read_csv(hr_year_csv)    
    f = plt.figure()
    plt.plot(data["yearID"], data["HR"], "r.-")
    plt.grid(True)
    plt.title("Number of Homeruns vs Years")
    plt.xlabel("Year")
    plt.ylabel("Number of Homeruns")
    return f


if __name__ == "__main__":
    filename = "../data/hr_year.csv"
    imagename = "matplot.png"
    f = lineplot(filename)
    f.savefig(imagename, bbox_inches='tight')
    f.show()
