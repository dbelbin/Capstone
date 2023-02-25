The intent of this product is the provide users with the ability to visualize the impact of specific features on home prices and be able to predict the 
value of a house in the City of Phoenix based on user inputs. The inputs available to the end user are zipcode, number of bedrooms, number of bathrooms, square
footage of the house, square footage of the lot, the year the house was built, whether the property has a pool and whether the property is associated with an HOA.
The data used to build the model was obtained through manual downloads from Redfin.com downloaded in batches and then loaded into python where it was cleaned and analyzed
using standard data exploratory analysis. Multiple models were tested and the Random Forest Regression model was choosen with the highest r^2 and lowest MAE of the tested
models. Once the model was chosen, the parameters were tuned to increase the accuracy. The streamlit portion of the model was built in multiple python pages and the model 
is deployed on streamlit cloud. Within the GitHub repository is a digigal poster representing the project, a user guide for the Streamlit app, as well as a system administrator guide to update and maintain the app.
