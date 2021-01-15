def get_out_slope_name(pred_days_list):
    out_slope_name = []
    for pred_days in pred_days_list:
        slope_name = "slope_"+str(pred_days)
        out_slope_name.append(slope_name)
    return out_slope_name



