from argparse import ArgumentParser
from PIL import Image
from matplotlib import pyplot
from matplotlib.figure import SubFigure
from skimage import io, exposure


def get_combined_histogram(filePath : str):
    with Image.open(filePath) as image:
        mixedHistogram = image.histogram()[:768]
        return [sum(mixedHistogram[i::256]) for i in range(256)]
        

def plot_histograms(subfigure : SubFigure, histograms : list[list]):
    plots = subfigure.subplots(len(histograms), 1)
    for index, plot in enumerate(plots):
        plot.stairs(histograms[index], fill=True)
        plot.set_xticks([0, 255])
        plot.set_yticks([])

parser = ArgumentParser()

parser.add_argument("--file", required=True, help="File to analyze")
args = parser.parse_args()

rgbHistogram = get_combined_histogram(args.file)
skImage = io.imread(args.file)
separatedHistograms = exposure.histogram(skImage, channel_axis=2)[0][:3] # we actually could've done the same by using pillow but however 

resultHistogram = [rgbHistogram]
resultHistogram.extend(separatedHistograms)

figure = pyplot.figure()
subfigures = figure.subfigures(1, 2)
leftPlot = subfigures[0].subplots(1, 1)
leftPlot.set_axis_off()
leftPlot.imshow(skImage)

plot_histograms(subfigures[1], resultHistogram)
pyplot.show()