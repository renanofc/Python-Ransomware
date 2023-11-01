
Para testar o Ransomware em sua máquina:

* edite as linhas 49 e 140 no arquivo ransomware.py com seus próprios caminhos absolutos etc para fins de teste e para que você possa usar a pasta localRoot

* [ATTACKER] Execute o script RSA para gerar duas chaves, uma chave privada e uma chave pública

* [TARGET] Execute o script ransomware - os arquivos .txt do localRoot serão criptografados agora

* [ATTACKER] Execute o arquivo de descriptografia da chave fernet para descriptografar o arquivo EMAIL_ME.txt (deve estar em sua área de trabalho), isso lhe dará um arquivo PUT_ME_ON_DESKTOP.txt, uma vez que você coloque isso na área de trabalho, o ransomware descriptografará os arquivos do localRoot naquele diretório

### Criado com
* Python 3.7 - https://www.python.org/

#### Aviso

> Esta ferramenta é apenas para fins de teste e acadêmicos e só pode ser usada onde houver estrito consentimento. Não a use para
> fins ilegais! É responsabilidade do usuário final obedecer a todas as leis locais, estaduais e federais aplicáveis. Os desenvolvedores não assumem
> nenhuma responsabilidade e não são responsáveis por qualquer uso indevido ou dano causado por esta ferramenta e software em geral.

#Python#Ransomware#Malware
