def cetak_info(**kwargs):
    for kunci, nilai in kwargs.items():
        print(f"{kunci} : {nilai}")
cetak_info(nama="Arya", umur=20, pekerjaan="Front End Developer and UI UX Designer") 