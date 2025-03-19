import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer


pd.options.display.float_format = '{:20.2f}'.format
pd.set_option('display.max_columns', 999)

path="dataset/cocktail_dataset.json"

def get_data():
    df = pd.read_json(path)
    return df
    
def extract_ingredient_names(ingredient_list):
    return [ingredient['name'] for ingredient in ingredient_list]

def process_data():
    df = get_data()
    df = df.drop(columns=['id','imageUrl',
                          'createdAt','updatedAt'])
    
    df['ingredient_names'] = df['ingredients'].apply(lambda x:
                                                     extract_ingredient_names(x))
    df['num_ingredients'] = df['ingredient_names'].apply(len)
    
    vectorizer = CountVectorizer(tokenizer=lambda x: x,
                                 token_pattern=None, lowercase=False)

    ingredient_matrix = vectorizer.fit_transform(df['ingredient_names'])

    ingredient_df = pd.DataFrame(ingredient_matrix.toarray(), 
                                 columns=vectorizer.get_feature_names_out())
    
    ingredient_df['num_ingredients'] = df['num_ingredients']

    ingredient_df['alcoholic'] = df['alcoholic']

    category_dummies = pd.get_dummies(df['category'], prefix='',
                                      prefix_sep='')
    ingredient_df = pd.concat([ingredient_df, category_dummies],
                               axis=1)

    glass_dummies = pd.get_dummies(df['glass'], prefix='', prefix_sep='')
    ingredient_df = pd.concat([ingredient_df, glass_dummies], axis=1)

    return ingredient_df

if __name__ == "__data__" :
    df = get_data()
    df.info() #Sprawdzam czy są braki danych
    print(df.head(5)) #Sprawdzam czy tagi są poprawne
    print(df.tail(5)) #Sprawdzam od końca czy tagi są poprawne
    df['glass'].unique() #Sprawdzam unikalne wartości w kolumnie glass
    df['category'].unique() #Sprawdzam unikalne wartości w kolumnie category
    df['alcoholic'].unique() #Sprawdzam unikalne wartości w kolumnie alcoholic
    df = process_data()
    df.info()

  

   