import turicreate
import os

#load images in

data = turicreate.image_analysis.load_images("images/")

#define labels
#these labels are what will be return by the model

data["label"] = data["path"].apply(lambda path: os.path.basename(os.path.dirname(path)))

#Save to SFrame which is like a dictionary

data.save("dog_classifier.sframe")

# Now let's train our model! First we need to split our data into training and testing
# This helps us determine our prediction power and avoid overfitting

#load the sframe
data = turicreate.SFrame("dog_classifier.sframe")

#Split into 75%, 25% Split

training, testing = data.random_split(0.75)

#Let's create and train our model!
#This line tells turi to use the training data and predict the labels using the restnet model

classifier = turicreate.image_classifier.create(training, target="label", model="resnet-50")

#
res = classifier.evaluate(testing)
print(res["accuracy"])

classifier.save("dog_classifier.model")
classifier.export_coreml("dog_classifier.mlmodel")
