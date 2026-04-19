// ================================================================
// INSTRUCCIONES PARA CONFIGURAR FIREBASE:
// 1. Ve a https://console.firebase.google.com
// 2. Haz clic en "Agregar proyecto" y dale un nombre (ej: bomberos-b120)
// 3. Ve a Configuración del proyecto (ícono engranaje) > General
// 4. En "Tus apps" haz clic en el ícono </> (Web)
// 5. Registra la app y copia los valores aquí abajo
// 6. Activa Authentication > Método de inicio > Correo/Contraseña
// 7. Activa Firestore Database > Crear base de datos (modo producción)
// 8. En Firestore > Reglas, pega las reglas que están más abajo
// ================================================================

const firebaseConfig = {
    apiKey:            "AIzaSyBxqZN0K49ABUMSd6PqWFTXrGuSAvWyF2E",
    authDomain:        "bomberos-b120.firebaseapp.com",
    projectId:         "bomberos-b120",
    storageBucket:     "bomberos-b120.appspot.com",
    messagingSenderId: "207435151529",
    appId:             "1:207435151529:web:3856d685a15d607efe91b8"
};

firebase.initializeApp(firebaseConfig);
const db   = firebase.firestore();
const auth = firebase.auth();

// ================================================================
// REGLAS DE FIRESTORE
// Copia esto en: Firebase Console > Firestore Database > Reglas
// ================================================================
/*
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {

    // Noticias: cualquiera puede leer, solo admins pueden escribir
    match /noticias/{doc} {
      allow read: if true;
      allow write: if request.auth != null &&
        get(/databases/$(database)/documents/usuarios/$(request.auth.uid)).data.rol == 'admin';
    }

    // Usuarios: cada uno lee/crea su propio doc; admins leen y editan todos
    match /usuarios/{uid} {
      allow read, update: if request.auth != null && (
        request.auth.uid == uid ||
        get(/databases/$(database)/documents/usuarios/$(request.auth.uid)).data.rol == 'admin'
      );
      allow create: if request.auth != null && request.auth.uid == uid;
      allow list: if request.auth != null &&
        get(/databases/$(database)/documents/usuarios/$(request.auth.uid)).data.rol == 'admin';
    }
  }
}
*/
