import matplotlib.pyplot as plt

x=["January","February", "March","April","May","June",
   "July","August","September","October","November","December"
    ]

y_2024=[37, 12, 45, 8, 29, 16, 50, 3, 24, 41, 19, 33]
y_2025=[14, 42, 7, 31, 25, 48, 3, 19, 36, 11, 27, 45]

plt.plot(x,y_2024,label="2024",marker="o",color="green")
plt.plot(x,y_2025, label="2025",marker="s",linestyle="--",color="red")

plt.legend(["Number of people in 2024","Number of people in 2025"], loc="upper left")
plt.grid(True)

plt.xlabel('Months')
plt.ylabel('Number of People')
plt.title('Testovi i bodovi')
plt.annotate("Vacation",xy=("August",19),
             xytext=("August",30),
             arrowprops=dict(facecolor="black", shrink=0.05),
             )
plt.scatter("August",19,s=100,zorder=5,color="black")




plt.show()
