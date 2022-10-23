import pyrebase, firebase_config, re
from   typing              import Any
from   requests.exceptions import HTTPError


class User(HTTPError):
    def __init__(self) -> None:
        super().__init__()

        self.__email     : str  = ''
        self.__token     : str  = ''
        self.__registered: bool  = False
        self.errno       : HTTPError = HTTPError()


    """
    Wrapper das funções de criação cria um novo usuário com verificação

    create_new_user:
        >> e-mail: String   # Qualquer tipo de e-mail que atendas formato de um
        >> passwd: String   # O password digitado pelo usuário
        << Boolean          # Se tudo correr bem, retorna Verdadeiro
    """
    def create_new_user(self, email: str, passwd: str ) -> bool:
  
        # Verifica antecipadamente se o e-mail esta formatado corretamentes antes
        # da requisição para o server do Firebase.
        if self.check_email(email) :

            # Tenta criar um novo usuário
            try:
                firebase = pyrebase.initialize_app(firebase_config.firebaseConfig)
                # Registra os dados requisitados
                self.__set_responde(
                    firebase.auth().create_user_with_email_and_password(email, passwd)
                )
                return True
            except HTTPError as e:
                self.errno = e
                print(e)
        return False



    """
    Verifica e retornar um usuário já cadastrado e um wrapper da mesma
    função nativa no Firebase.
    """
    def get_sign_user(self, email: str, passwd: str) -> bool:

        if self.check_email(email) and self.check_passwd(passwd):

            # Tenta criar retornar um usuário já cadastro
            try:
                firebase = pyrebase.initialize_app(firebase_config.firebaseConfig)

                # Registra os dados requisitados
                self.__set_responde(
                    firebase.auth().sign_in_with_email_and_password(email, passwd)
                )
                return True
            except HTTPError as e:
                self.errno = e
                print(e)
        return False



    """
    Verifica o e-mail atraves de expressão regular antes de um resquest para o Firebase

    check_email:
        >> email: String   # Qualquer tipo de e-mail que atendas formato de um
        << Boolean
    """
    def check_email(self, email: str):
        return re.findall(r'[\w\.-]+@[\w\.-]+\.[\w]+', email) and len(email) < 256



    """
    Verifica se o password possuí alphanérico case caixa alta, baixa e simbolos
    entre 8 a 20 caracteres

    check_email:
        >> passwd: String   # Toda senha que segue a regra acima
        << Boolean
    """
    def check_passwd(self, passwd: str) -> bool:
        return re.findall(r'^(?=.*?[aA0-9Zz])(?=.*?[#?!@$ %^&*-]).{8,}', passwd) == passwd

    
    
    """
    Torna o e-mail registrado da classe 
    """
    def get_email(self) -> str:
        return self.__email



    """
    Mantem reservado o token de autenticação ao invés da senha.
    """
    def __id_token(self) -> str:
        return self.__token



    """
    Prepara todos os dados importantes para serem armazenados na class

    __set_response[private]
        >> auth: firebase.Auth   # Os dados do resquest ao Firebase
        << None
    """
    def __set_responde(self, auth) -> None:
        print(auth)
        self.__email     = auth['email'     ]
        self.__token     = auth['idToken'   ]
        self.__registered= True



    """
    Retorna se tem algum registro armazenado em formato de texto

    is_registered:
        << String(Yes|No)
    """
    def is_registered(self) -> str :
        if self.__registered == True:
            return 'Yes'
        return 'No'

    def __str__(self) -> str:
        return 'User e-mail: ' + self.get_email() + '\n' + self.is_registered()
        
