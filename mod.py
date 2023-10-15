 
import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()

# defining the function which will make the prediction using the data which the user inputs 
def prediction(Education, Marital_Status, DOB,Incomes,Kidhome,Teenhome,Purchases,Expense,Recency,Campaign,Complain, Response):   
 
    # Pre-processing user input    
    
    if Education == "Basic":
        Education = 0
        
    elif Education == "Graduated":
        Education = 1
        
    elif Education == "PHD":
        Education = 2
#*****************************************#      
    if Marital_Status == "Single":
        Marital_Status = 0
    
    elif Marital_Status == "Relationship":
        Marital_Status = 1
#*****************************************#        
    if Incomes == "Below 25000":
        Incomes = 1
    
    elif Incomes == "Income 25000-50000":
        Incomes = 2
        
    elif Incomes == "Income 50000-100000":
        Incomes = 3
        
    elif Incomes == "Above 100000":
        Incomes = 0
        

#*****************************************# 

    if Campaign == "Accepted 0 Campaign":
        Campaign = 0
    
    elif Campaign == "Accepted 1 Campaign":
        Campaign = 1
        
    elif Campaign == "Accepted 2 Campaign":
        Campaign = 2
        
    elif Campaign == "Accepted 3 Campaign":
        Campaign = 3  
        
    elif Campaign == "Accepted 4 Campaign":
        Campaign = 4
        


#*****************************************#    
    if Response == "YES":
        Response = 1
    
    elif Response == "NO":
        Response = 0

#*****************************************#      
    if Complain == "YES":
        Complain = 1
    
    elif Complain == "NO":
        Complain = 0
  #*****************************************#     

  #*****************************************# 
        
        
    prediction = classifier.predict( 
        [[Education, Marital_Status,DOB, Incomes, Kidhome,Teenhome,Purchases,Expense,Recency,Campaign,Complain, Response]])
            
    if prediction == 0:
        pred = 'cluster 0'
   
    elif prediction == 1:
        pred = 'cluster 1'
    
    elif prediction == 2:
        pred = 'cluster 2'
        
    elif prediction == 3:
        pred = 'cluster 3'
    
    return pred
   
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:Orange;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Model Deployment</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
    
    # following lines create boxes in which user can enter data required to make prediction 
    
    Education = st.selectbox("Education",("Basic","Graduated","PHD"))
    
    Marital_Status = st.radio("Marital_Status: ", ('Single', 'Relationship'))
    if (Marital_Status == 'Single'):
        st.success("Single")
    elif (Marital_Status == 'Relationship'):
        st.success("Relationship")
    
    DOB = st.slider("Select DOB", 1930, 2021)
    st.text('Selected: {}'.format(DOB)) 
    
    Incomes = st.selectbox("Incomes",("Below 25000", "Income 25000-50000", "Income 50000-100000","Above 100000")) 
   
    Kidhome = st.text_input("Kidhome")
    
    Teenhome = st.text_input("Teenhome") 
    
    Purchases= st.slider("NUmber of Purchase Made", 0, 50)
    st.text('Selected: {}'.format(Purchases)) 
    
    Expense = st.slider("Select Monthly Expense", 0, 3000)
    st.text('Selected: {}'.format(Expense)) 
    
    Recency= st.slider("last Purchase", 0, 100)
    st.text('Selected: {}'.format(Recency)) 

    Campaign =st.selectbox("Campaign",("Accepted 0 Campaign","Accepted 1 Campaign","Accepted 2 Campaign","Accepted 3 Campaign","Accepted 4 Campaign"))
    
    Complain = st.selectbox("Complain",("YES","NO"))
    
    Response = st.selectbox("Accepted the offer in the last campaign",("YES","NO"))
    
    result =""
          
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Education, Marital_Status,DOB, Incomes, Kidhome,Teenhome,Purchases,Expense,Recency, Campaign,Complain, Response) 
        st.success('Common cluster is {}'.format(result))
   
     
if __name__=='__main__': 
    main()
