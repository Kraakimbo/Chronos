# Chronos — app mobile (iOS / Android)

Ce dossier contient un wrapper [Capacitor](https://capacitorjs.com/) qui embarque
le site Chronos déjà déployé sur Render dans une vraie app native, publiable sur
l'App Store et Google Play. **Ce n'est pas une réécriture** : l'app mobile
charge les mêmes pages que le site (`server.url` dans `capacitor.config.json`),
donc tout le backend Flask reste la seule source de vérité — une seule
codebase à maintenir pour le contenu, l'auth, la gamification, etc.

## Avant de construire

1. **Vérifie l'URL du site** dans `capacitor.config.json` (`server.url` et
   `server.allowNavigation`). Actuellement : `https://chronos-dqh6.onrender.com`.
   Si l'URL Render change (nouveau service, domaine personnalisé), mets ces
   deux champs à jour puis relance `npx cap sync`.
2. **Choisis un vrai `appId`** dans `capacitor.config.json` (actuellement
   `com.chronos.app`, un identifiant générique à remplacer avant soumission).
   Ce doit être un identifiant unique de type reverse-domain
   (ex. `com.tonstudio.chronos`), identique sur iOS (bundle ID App Store
   Connect) et Android (`applicationId`), et **ne doit plus changer après la
   première publication**.
3. Icônes et splash screen sont déjà générés dans `resources/` (palette
   Chronos : fond `#FAF9F7`, trait `#735C00`, même dessin que
   `app/static/favicon.svg`) et synchronisés dans `android/` et `ios/` via
   `@capacitor/assets`. Pour les régénérer après une modif de
   `resources/icon.png` ou `resources/splash.png` :
   ```bash
   npx capacitor-assets generate --iconBackgroundColor '#FAF9F7' --iconBackgroundColorDark '#FAF9F7' --splashBackgroundColor '#FAF9F7' --splashBackgroundColorDark '#FAF9F7'
   ```

## Installer les dépendances

```bash
cd mobile
npm install
```

## Android (buildable sur Linux/Mac/Windows avec Android Studio)

```bash
npx cap sync android
npx cap open android
```

Android Studio s'ouvre sur `mobile/android`. Ensuite : **Build → Generate
Signed App Bundle**, créer/choisir un keystore, publier l'`.aab` généré sur la
[Google Play Console](https://play.google.com/console) (compte développeur :
25 $ une seule fois).

> Non vérifié dans l'environnement actuel : le projet Gradle a été généré et
> sa structure est valide, mais aucun SDK Android n'est installé ici, donc la
> compilation réelle de l'APK/AAB n'a pas pu être testée dans ce sandbox.

## iOS (nécessite un Mac avec Xcode)

```bash
cd mobile
npx cap sync ios      # nécessite CocoaPods installé sur le Mac (`sudo gem install cocoapods`)
npx cap open ios
```

Xcode s'ouvre sur `mobile/ios/App/App.xcworkspace`. Ensuite, comme indiqué
dans le README principal :

1. Compte [Apple Developer Program](https://developer.apple.com/programs/) (99 $/an).
2. Dans **App Store Connect**, créer la fiche app avec le même bundle ID que
   `capacitor.config.json`.
3. Dans Xcode : lier ton compte Apple Developer (signature automatique),
   **Product → Archive**, puis envoyer l'archive à App Store Connect via
   l'Organizer.
4. Compléter la fiche (captures d'écran, description, compte de test si
   nécessaire) et soumettre pour revue (généralement 24–48 h).

> Non vérifié dans l'environnement actuel : ce sandbox Linux n'a ni Xcode ni
> CocoaPods, donc seule la génération du projet a pu être testée — pas la
> compilation ni la signature, qui doivent être faites sur un Mac.

## Limites de l'approche wrapper à connaître

- L'app nécessite une connexion réseau pour fonctionner (elle charge les
  pages du site Render en direct) — pas de mode hors-ligne réel.
- Le plan gratuit Render peut mettre le service en veille après inactivité :
  au premier lancement de l'app après une pause, l'utilisateur peut attendre
  quelques secondes le temps que le service se réveille.
- Les stores (Apple en particulier) peuvent rejeter une app qui n'est
  qu'une redirection vers un site sans valeur ajoutée native perçue. Pour
  limiter ce risque : les plugins `@capacitor/status-bar` et
  `@capacitor/splash-screen` sont déjà branchés pour une sensation native
  (splash animé, barre de statut stylée) ; ajouter des notifications push,
  un mode hors-ligne ou d'autres capacités natives via des plugins Capacitor
  renforcerait le dossier de soumission si besoin.
