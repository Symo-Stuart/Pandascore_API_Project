import pandas as pd

def json_transformation(results):
    
    # Data Manipulation
    sample_result = results[0]
    one_to_one_keys = [key for key in sample_result.keys() if type(sample_result[key]) != dict]
    one_to_many_keys = [key for key in sample_result.keys() if key not in one_to_one_keys]
    
    # One to One Transformation

    ## Iterate through the results
    result_dict = {key : [] for key in one_to_one_keys} 
    for resp in results:
        for key in one_to_one_keys:
            ## Get the value for a specific key in the dictionary
            value = resp[key]
            ## Add that value to a running list until you get all 100 records
            result_dict[key].append(value)
    
    ## One to Many Transformation
    many_result_dict = {}

    for key in one_to_many_keys:
        child_keys = sample_result[key].keys()
        for c_key in child_keys:
            updated_key = f"{key}_{c_key}"
            many_result_dict[updated_key] = []
    
    for resp in results:
        for key in one_to_many_keys:
            # Get the child keys
            if resp[key] is not None:
                child_keys = resp[key].keys()
                for child in child_keys:
                    value = resp[key][child]
                    new_col_name = f'{key}_{child}'
                    many_result_dict[new_col_name] = value
    
    frames = [pd.DataFrame.from_dict(result_dict), pd.DataFrame(many_result_dict, index=[0])]
    frame_df =  pd.concat(frames, axis=1)
    frame_df = frame_df.loc[:, ~frame_df.columns.duplicated()].copy()
    return frame_df
