

def 


for i in stock_index:
    html1 = find_url(i)
    raw_data = get_from_url(html1)
    clean_data = clean_data(raw_data)
    save_data = save_data(clean_data)
    copy_data = copy_to_current_folder()
