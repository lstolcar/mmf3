import numpy as np

def save_dict_columns(filename, data_dict):
    titles = list(data_dict.keys())
    columns = list(data_dict.values())
    
    # Pronađi maksimalni broj redova
    n = max(len(col) for col in columns)
    
    # Odredi optimalnu širinu za svaki stupac
    column_widths = []
    for title, col in zip(titles, columns):
        # Širina naslova
        title_width = len(title)
        
        # Širina najšireg broja (formatiranog na 6 decimala)
        # Ispravka: koristimo len(col) > 0 umjesto if col za provjeru
        if len(col) > 0:
            max_num_width = max(len(f"{x:.6f}") for x in col)
        else:
            max_num_width = 0
            
        # Uzmi veću vrijednost
        column_widths.append(max(title_width, max_num_width))
    
    # Kreiraj tabelu
    table = np.full((n + 1, len(columns)), "", dtype=object)
    
    # Postavi naslove (centrirane iznad stupaca)
    for j, title in enumerate(titles):
        table[0, j] = f"{title:^{column_widths[j]}}"
    
    # Postavi podatke
    for j, col in enumerate(columns):
        col_array = np.asarray(col)
        for i, value in enumerate(col_array):
            table[i + 1, j] = f"{value:{column_widths[j]}.6f}"
    
    # Spremi u file
    with open(filename, "w", encoding='utf-8') as f:
        for i in range(table.shape[0]):
            # Koristi 4 razmaka između stupaca za bolju čitljivost
            line = "    ".join(table[i, :])
            f.write(line + "\n")