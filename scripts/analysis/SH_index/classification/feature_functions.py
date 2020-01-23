import featuretools as ft

def feature_columns():
    '''
    make the feature column name to put into 
    the featuretools to make features
    '''
    feature_col = ['index','mv_avg5', 'mv_avg10', 'mv_avg15',
               'mv_avg20', 'mv_avg30', 'mv_avg40', 'mv_avg50',
               'mv_avg60', 'mv_avg120',
               'mv_avg150', 'mv_avg200', 'mv_avg300']  
    close_fea = []
    for i in range(1,30):
        close_fea.append('close'+str(i))
    fea_col = feature_col+close_fea
    return fea_col

def make_features(df1,fea_col):
    ''' 
    dataframe to make feature columns
    '''
    df_fea = df1[fea_col]
    es = ft.EntitySet(id = 'sales')
    es.entity_from_dataframe(entity_id = 'bigmart', dataframe = df_fea, index = 'index')
    #primitives[primitives['type'] == 'transform'].head(100)
    #primitives[primitives['type'] == 'aggregation'].head(10)
    feature_matrix,feature_names = ft.dfs(entityset = es,
	    target_entity ='bigmart',
	    max_depth = 2,
	    agg_primitives=['mean','max','std'],
	    trans_primitives = ['less_than'],
	    verbose = 1,
	    n_jobs = 1)
    return feature_matrix,feature_names
