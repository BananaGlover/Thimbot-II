import random
import json
from matplotlib import pyplot as plt
import matplotlib.transforms as transforms
from datetime import datetime

DATA_PATH = "database\market_log.json"

#constants
UPDATE_PER_HOUR = 60

MARKET_CEIL = 5000
MARKET_FLOOR = 1000
CENTER_MASS = 2500

#DOCUMENT SHITTY CODE

def get_hour_data(hour: int) -> list[int]:
    with open(DATA_PATH, "r") as data:
        lst: list[int] = json.load(data)[-(UPDATE_PER_HOUR*hour):]
    return lst

    

def get_latest_data() -> int:
    with open(DATA_PATH, "r") as data:
        latest = json.load(data)[-1]
    return latest



def add_data(new_data: int):
    """add passed data to market_log.json"""

    data = get_data()

    if len(data) == UPDATE_PER_HOUR*24:
        data.pop(0)
        data.append(new_data)
    elif len(data) > UPDATE_PER_HOUR*24:
        data = data[-UPDATE_PER_HOUR*24:]
    else:
        data.append(new_data)

    dump_data(data)
    return

def get_data() -> list[int]:
    with open(DATA_PATH, 'r') as data_r:
        return json.load(data_r)

def dump_data(new_data: list[int]):
    with open(DATA_PATH, 'w') as data_w:
        json.dump(new_data, data_w, indent=4)
    return


def generate_graph(hour: int):
    """Uses Matplotlib to generate a graph of last x hours"""

    #x and y data sets
    data_x = list(range(UPDATE_PER_HOUR*hour))
    data_y = get_hour_data(hour)

    #initialize fig and ax + style
    fig, ax = plt.subplots()
    plt.style.use("dark_background")

    #draw lines
    def plot_line(x: list[int], y: list[int], color: chr):
        ax.plot(x, y, color=color, linewidth=2.5)
    plt.grid(axis='y')

    #look if red or green lines + look for highest and lowest
    highest = data_y[0]
    lowest = data_y[0]
    current = data_y[-1]
    for x1, x2, y1, y2 in zip(data_x, data_x[1:], data_y, data_y[1:]):
        if y1 > y2:
            plot_line([x1, x2], [y1, y2], '#e63939') #red
        elif y1 < y2:
            plot_line([x1, x2], [y1, y2], '#87e36b') #green
        else:
            plot_line([x1, x2], [y1, y2], '#87e36b') #green

        if y1 > highest:
            highest = y1
        if y2 > highest:
            highest = y2
        
        if y1 < lowest:
            lowest = y1
        if y2 < lowest:
            lowest = y2

    #add title
    ax.set_title(f"TBC last {hour}H", fontname="Consolas", size=20)
    ax.title.set_color('white')

    #set lines to white
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white') 
    ax.spines['right'].set_color('white')
    ax.spines['left'].set_color('white')

    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    #draw highest, lowest and current
    ax.axhline(y=lowest, color='#e63939', linewidth="1.5", linestyle="--")
    ax.axhline(y=highest, color='#87e36b', linewidth="1.5", linestyle="--")
    ax.axhline(y=current, color='#5470f0', linewidth="1.5", linestyle="--")

    #add hightest and lowest text
    trans = transforms.blended_transform_factory(
    ax.get_yticklabels()[0].get_transform(), ax.transData)
    ax.text(1.025,highest, "{:.0f}".format(highest), color="#87e36b", transform=trans, 
        ha="left", va="center", size=11)
    ax.text(1.025,lowest, "{:.0f}".format(lowest), color="#e63939", transform=trans, 
    ha="left", va="center", size=11)
    ax.text(1.025,current, "{:.0f}".format(current), color="#5470f0", transform=trans, 
    ha="left", va="center", size=11)

    #add ands move "now" text
    ax.set_xlabel("now", color="white", fontname="Consolas", size=14)
    ax.xaxis.set_label_coords(.96, -0.025)

    #set y and x axis
    ax.set_yticks([*range(0, MARKET_CEIL+1, int(MARKET_CEIL/10))])
    ax.tick_params(axis='y', labelsize=11)
    ax.set_xticks([])

    #save image and close plt
    fig.savefig('./images/graph.png', transparent=True)
    plt.close()
    return



def evaluate(current: int) -> int:
    """returns new (modified) current"""

    #FIX THIS STINKY ASS CODE

    UP = 5
    DOWN = 5
    LUCKY = 1
    STABLE = 10

    up_sub, down_sub = 0, 0
    if current > CENTER_MASS: up_sub = 3 #favorise down
    elif current < CENTER_MASS: down_sub = 3 #favorise up

    tendancies = {
        "up++": ((200, 500), UP - up_sub),
        "up+": ((100, 200), UP - up_sub),
        "down--": ((-500, -200), DOWN - down_sub),
        "down-": ((-200, -100), DOWN - down_sub),
        "lucky": ((500, 750), LUCKY),
        "unlucky": ((-750, -500), LUCKY),
        "stable+": ((30, 100), STABLE),
        "stable-": ((-100, -30), STABLE)
    }

    odds = []
    for key in tendancies.keys():
        for i in range(tendancies[key][1]):
            odds.append(key)

    #TO DOCUMENT
    choice = random.choice(odds)
    tend = tendancies[choice][0]
    hop = random.randint(tend[0], tend[1])

    if current + hop >= MARKET_CEIL:
        #too big of jump
        new_current = MARKET_CEIL - random.randint(0, 15)
    elif current + hop < MARKET_FLOOR:
        #too small of jump
        new_current = MARKET_FLOOR + random.randint(0, 15)
    else:
        new_current = current + hop

    print(f"{get_latest_data()} +[{hop}] -> {new_current} || tendancy: {choice}")

    return new_current



def update():

    new_current: int = evaluate(get_latest_data())
    return add_data(new_current)