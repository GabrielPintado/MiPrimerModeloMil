import streamlit as st

st.set_page_config(page_title="Cipher App", page_icon="🔐")

st.title("🔐 Mensajería Secreta")
st.write("Usa una clave numérica para ocultar tus mensajes.")

# Creamos dos pestañas para organizar la app
tab1, tab2 = st.tabs(["🔒 Encriptar", "🔓 Descifrar"])

# Lógica del Cifrado César
def procesar_texto(texto, desplazamiento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # Aplicamos la fórmula: (posición + clave) % 26 letras del abecedario
            resultado += chr((ord(char) - base + desplazamiento) % 26 + base)
        else:
            resultado += char
    return resultado

with tab1:
    st.header("Ocultar mensaje")
    msg_original = st.text_input("Mensaje claro:", key="enc_input", placeholder="Hola, nos vemos a las 5")
    clave_enc = st.number_input("Elige tu clave secreta (un número):", min_value=1, value=5)
    
    if msg_original:
        encriptado = procesar_texto(msg_original, clave_enc)
        st.info("Copia este mensaje y envíalo:")
        st.code(encriptado, language=None)

with tab2:
    st.header("Leer mensaje secreto")
    msg_cifrado = st.text_input("Pega el mensaje raro aquí:", key="dec_input")
    clave_dec = st.number_input("Clave secreta del emisor:", min_value=1, value=5)
    
    if msg_cifrado:
        # Para descifrar, simplemente movemos el abecedario hacia atrás
        descifrado = procesar_texto(msg_cifrado, -clave_dec)
        st.success("Mensaje revelado:")
        st.write(f"### {descifrado}")

st.divider()
st.caption("Nota: Para que funcione, ambos deben usar el mismo número de clave.")
