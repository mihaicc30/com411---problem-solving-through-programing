import matplotlib.pyplot as plt

def read_data(filename):
  f = open(filename,"r")
  content = f.readlines()
  f.close()
  return content

def run():
  data = read_data("visual/subplots/temps.txt")
  fig, axes = plt.subplots(1,2)
  x = range(1,8,1)
  y = data
  axes[0].set_xlabel("days")
  axes[0].set_ylabel("temps")
  axes[1].set_xlabel("days")
  axes[1].set_ylabel("temps")
  axes[0].plot(x,y)
  axes[1].bar(x,y)

  plt.tight_layout()
  plt.show()

  
run()