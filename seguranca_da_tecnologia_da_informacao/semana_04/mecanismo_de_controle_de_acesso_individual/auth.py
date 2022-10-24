import pyrebase, firebase_config, re
from   typing              import Any
from   requests.exceptions import HTTPError


# ----------   class User    ----------
class User(HTTPError):
    """
    Classe para armazenar registros de um novo usuário, alterações
    ou guardar dados para manipulção

    Construtor dela é vazio

    user = User()

    """

    # ----------    __init__     ----------
    def __init__(self) -> None:
        super().__init__()

        self.__email     : str  = ''
        self.__token     : str  = ''
        self.__registered: bool  = False
        self.__errno       : HTTPError = HTTPError()

    # ---------- create_new_user ----------
    def create_new_user(self, email: str, passwd: str ) -> bool:
        """
        Wrapper das funções de criação cria um novo usuário com verificação

        create_new_user:
            >> e-mail: String   # Qualquer tipo de e-mail que atendas formato de um\n
            >> passwd: String   # O password digitado pelo usuário\n
            << Boolean          # Se tudo correr bem, retorna Verdadeiro\n
        """
  
        # Verifica antecipadamente se o e-mail esta formatado corretamentes antes
        # da requisição para o server do Firebase.
        if self.check_email(email) and self.check_passwd(passwd):

            # Tenta criar um novo usuário
            try:
                firebase = pyrebase.initialize_app(firebase_config.firebaseConfig)
                # Registra os dados requisitados
                self.__set_response(
                    firebase.auth().create_user_with_email_and_password(email, passwd)
                )
                return True
            except HTTPError as e:
                self.errno = e
                return False
        print('Verify is your e-mail our password are correct!')
        return False

    # ----------  get_sign_user  ----------
    def get_sign_user(self, email: str, passwd: str) -> bool:
        """
        Verifica e retornar um usuário já cadastrado e um wrapper da mesma
        função nativa no Firebase.
    
        create_new_user:
            >> e-mail: String   # Qualquer tipo de e-mail que atendas formato de um\n
            >> passwd: String   # O password digitado pelo usuário\n
            << Boolean          # Se tudo correr bem, retorna Verdadeiro
        """

        if self.check_email(email) and self.check_passwd(passwd):

            # Tenta criar retornar um usuário já cadastro
            try:
                firebase = pyrebase.initialize_app(firebase_config.firebaseConfig)

                # Registra os dados requisitados
                self.__set_response(
                    firebase.auth().sign_in_with_email_and_password(email, passwd)
                )
                return True
            except HTTPError as e:
                self.errno = e
                return False
        print('Verify is your e-mail our password are correct!')
        return False

    # ----------   check_email   ----------
    def check_email(self, email: str):
        """
        Verifica o e-mail atraves de expressão regular antes de um resquest para o Firebase

        check_email:
            >> email: String   # Qualquer tipo de e-mail que atendas formato de um\n
            << Boolean
        """
        return re.findall(r'[\w\.-]+@[\w\.-]+\.[\w]+', email) and len(email) < 256

    # ----------  check_passwd   ----------
    def check_passwd(self, passwd: str) -> bool:
        """
        Verifica se o password possuí alphanérico case caixa alta, baixa e simbolos
        entre 8 a 20 caracteres

        check_email:
            >> passwd: String   # Toda senha que segue a regra acima\n
            << Boolean
        """
        # 
        # ^  -> Inicio de Linha
        # (?=.*?[aA0-9Zz])    -> Busque 0 ou qalquer valor entre [a-z][A-Z][0-9]
        # (?!.*?[\ \n\r\t])   -> Ignore qualquer espaço branco 
        # (?=.*?[#?!@$%^&*-]) -> Busque 0 ou qalquer valor entre [ dentro dos colchetes ]
        # .{8, 100}$          -> minimo 8 máximo 100
        # $  -> Encerre no final da linha 
        #

        return re.findall(r'^(?=.*?[a-zA-Z0-9])(?!.*?[\ \r\t])(?=.*?[#?!@$%^&*-]).{8,}$', passwd) != []
    
    # ----------    get_email    ----------
    def get_email(self) -> str:
        """
        Torna o e-mail registrado da classe 
        """
        return self.__email

    # ----------   __id_token    ----------
    def id_token(self) -> str:
        """
        Mantem reservado o token de autenticação ao invés da senha.
        """
        return self.__token

    # ---------- __set_response  ----------
    def __set_response(self, auth) -> None:
        """
        Prepara todos os dados importantes para serem armazenados na class

        __set_response[private]
            >> auth: firebase.Auth   # Os dados do resquest ao Firebase\n
            << None
        """
        self.__email     = auth['email'     ]
        self.__token     = auth['idToken'   ]
        self.__registered= True

    def email_verify(self):
        firebase = pyrebase.initialize_app(firebase_config.firebaseConfig)
        return firebase.auth().get_account_info(self.id_token())['users'][0]['emailVerified']

    # ----------  is_registerd   ----------
    def is_registered(self) -> str :
        """
        Retorna se tem algum registro armazenado em formato de texto

        is_registered:
            << String(Yes|No)
        """
        if self.__registered == True:
            return 'Yes'
        return 'No'


    def print_errno(self) -> None:
        print(self.__error)

    def get_errno(self) -> None:
        return self.__errno

    # ----------     __str__     ----------
    def __str__(self) -> str:
        return 'User e-mail: ' + self.get_email() + '\nRegistered :' + self.is_registered() + '\n'

        
