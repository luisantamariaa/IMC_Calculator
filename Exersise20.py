#Aplication to calculate the IMC "Indice de Masa Corporal" at 2hr 07mins 49sec

#To create an App to calculate IMC "Indice de Masa Corporal"

# IMC = peso / (altura)x(altura)

print("Please indicate your weight:")
weight=input()

print("Please indicate your height:")
height=input()

IMC= int(weight) / ((float(height))*(float(height))) #el peso es int bc is un valor entero. Para la altura usamos float ya que puede usar decimales. It is important to declare the correct
#use of parenthesis to correlate the calculations prevalecense or calculation priority 

print("Your IMC is:",IMC)


