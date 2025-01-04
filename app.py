import customtkinter as ctk 

ctk.set_appearance_mode('dark')



def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()


    if usuario == 'Moisés' and senha == 'Moises123':
        resultado_login.configure(text='Login feito com sucesso!',
                                  text_color='green')
    else:
        resultado_login.configure(text='Usuário ou senha inválidos!',
                                  text_color='red')
        
app = ctk.CTk()
app.title('Sistema de Login')
app.geometry('300x300')




label_usuario = ctk.CTkLabel(app,text='Usuário')
label_usuario.pack(pady=10)

campo_usuario = ctk.CTkEntry(app,placeholder_text='Digite seu usuário')
campo_usuario.pack(pady=10)

label_senha= ctk.CTkLabel(app, text='Senha')
label_senha.pack(pady=10)

campo_senha = ctk.CTkEntry(app,placeholder_text='Digite sua senha:')
campo_senha.pack(pady=10)

botao__login = ctk.CTkButton(app, text='Login',command=validar_login)
botao__login.pack(pady=10)

resultado_login = ctk.CTkLabel(app,text='')
resultado_login.pack(pady=10)



app.mainloop()