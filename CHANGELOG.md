## 1.0.0 (2024-05-17)


### ⚠ BREAKING CHANGES

* change package name
* **docs:** moved the `Docusaurus` folder up one level, removed all other documentation (now all inside of Docusaurus subpages)

### Features

* **CI:** automated pylint tests on push ([c794037](https://github.com/f-aguzzi/tesi/commit/c794037807d060b7450e6c720329d69b3cb6f445))
* completed use case diagram ([63ce9e4](https://github.com/f-aguzzi/tesi/commit/63ce9e4744494c7622de7ca52e189a4a6f7768f0))
* **readme:** created readme with badges ([6691d18](https://github.com/f-aguzzi/tesi/commit/6691d1814f23c20376a7e04980375be3bb6f4ce3)), closes [#5](https://github.com/f-aguzzi/tesi/issues/5)
* first draft of project plan ([8adb87d](https://github.com/f-aguzzi/tesi/commit/8adb87d9c4cb66e386c94cf7132601074c541962))
* implemented k-nearest neighbors ([63228a2](https://github.com/f-aguzzi/tesi/commit/63228a26b208bc7e6f4d605aada2cfffbfb87f29)), closes [#12](https://github.com/f-aguzzi/tesi/issues/12)
* **tests:** implemented lldf module unit tests ([9311da4](https://github.com/f-aguzzi/tesi/commit/9311da4c1ba60c5a9d35cc24e9ab70c2c8f58cf4))
* implemented LR class ([ec3582c](https://github.com/f-aguzzi/tesi/commit/ec3582c8941b8db97780504988c2a2b8567285e4)), closes [#2](https://github.com/f-aguzzi/tesi/issues/2)
* implemented pca and lda ([c59147f](https://github.com/f-aguzzi/tesi/commit/c59147f8e349fe93c800e3aa3ef0605263b7950a))
* implemented PLSDA ([af35254](https://github.com/f-aguzzi/tesi/commit/af3525490a9638e608d0bfa8719d90a078d504a8)), closes [#10](https://github.com/f-aguzzi/tesi/issues/10)
* implemented SVM ([a3e95bc](https://github.com/f-aguzzi/tesi/commit/a3e95bc75529fa91ba2f00ef3d78dc3e50a57e89))
* **docs:** move all documentation into docusaurus ([e1f2e7d](https://github.com/f-aguzzi/tesi/commit/e1f2e7dd95354809b2285664798e657d0cef3f8f))
* **docs:** sequence and process UML diagrams ([bec766f](https://github.com/f-aguzzi/tesi/commit/bec766f1cf3d846353b204f254199e771219536d))
* **Colab:** set up notebook for Colab demo ([638a67f](https://github.com/f-aguzzi/tesi/commit/638a67f213b138ad1e48fae3ef06a41f67de35ef)), closes [#4](https://github.com/f-aguzzi/tesi/issues/4)


### Bug Fixes

* **CI/CD:** add missing configuration files ([ebe28d5](https://github.com/f-aguzzi/tesi/commit/ebe28d547ff7c6531f5b3faf365922216a3e76e8))
* **CI:** added conditional activation of workflows ([aa4e916](https://github.com/f-aguzzi/tesi/commit/aa4e91610c9650ab79a9f6df8bd7815170257efc)), closes [#6](https://github.com/f-aguzzi/tesi/issues/6)
* **pylint:** added requirements, increased scores ([bef1cdf](https://github.com/f-aguzzi/tesi/commit/bef1cdfa5839cffbbb908489123ccbcb02459582))
* added test cases for LLDF, PCA, LDA, SVM ([0ba2f26](https://github.com/f-aguzzi/tesi/commit/0ba2f26ba81cf4dae44849730385c0dfabbac73e)), closes [#3](https://github.com/f-aguzzi/tesi/issues/3)
* **CI:** broken rye sync in workflows ([3c8482b](https://github.com/f-aguzzi/tesi/commit/3c8482bcd01191745eb1dba05096520664582701))
* **LLDF:** datasheet export now works properly ([131d3db](https://github.com/f-aguzzi/tesi/commit/131d3db113c9c925223357a4b4b5ea57ee8c6929))
* **CI:** fixed workflow triggers ([6069c89](https://github.com/f-aguzzi/tesi/commit/6069c89676e29c6bf795c2dc8851922a1ad3189a))
* gh_pages workflow ([0a6fc43](https://github.com/f-aguzzi/tesi/commit/0a6fc4373ea18870c47e16d12839462c1ef5fb45))
* **notes:** merged obsidian duplicate folders ([234b200](https://github.com/f-aguzzi/tesi/commit/234b200ecf7a468a72f441a19966621de733c6ac))
* removed pycache, changed favicon ([a6407f6](https://github.com/f-aguzzi/tesi/commit/a6407f662fa286be8bb78d8344cfb73e8f041e8e))
* **CI/CD:** set GitGub token ([05a4440](https://github.com/f-aguzzi/tesi/commit/05a444042d42f3b95dc464f056acd707592d395b)), closes [#15](https://github.com/f-aguzzi/tesi/issues/15)
* **docs:** spelling mistakes ([a10d512](https://github.com/f-aguzzi/tesi/commit/a10d5125d196ebc22304106090ebef6257aa1076))
* **notebook:** update broken links, remove checkpoints ([d8723a1](https://github.com/f-aguzzi/tesi/commit/d8723a1cdc363ccb5ac79692fe4c147225038e95)), closes [#14](https://github.com/f-aguzzi/tesi/issues/14) [#13](https://github.com/f-aguzzi/tesi/issues/13)
* **tests:** various mistakes in workflow script ([3d63d37](https://github.com/f-aguzzi/tesi/commit/3d63d3736bd8eb21da427c4b349d435f21ddae93))


### chore

* change package name ([bd5006d](https://github.com/f-aguzzi/tesi/commit/bd5006d2d1adcc440c4347f945a0a01300f96aa4))
* **rye:** readapt project structure to rye ([38c66e6](https://github.com/f-aguzzi/tesi/commit/38c66e69993510247e6cd3b6f0c75a38f35d341e))
* **testing:** set up automated unit tests ([73b399e](https://github.com/f-aguzzi/tesi/commit/73b399e4b84b6e11ebcf5fdb1601e76b39d5ff97))
* **CI/CD:** set up automatic releases ([8536dc2](https://github.com/f-aguzzi/tesi/commit/8536dc2f26ae66ba658867a7a66c6212ba56dea6))
* **obsidian:** set up devlogs, kanban and uml ([f8ec9af](https://github.com/f-aguzzi/tesi/commit/f8ec9af71809b1bcf5c20f531364ab6dad10b0f4))
* **docs:** set up docusaurus and gh-pages ([3c957e8](https://github.com/f-aguzzi/tesi/commit/3c957e883c2272653b6510d0c8b1094d1edb1ee0))
* set up project structure ([040fcfa](https://github.com/f-aguzzi/tesi/commit/040fcfa8ea804cbd6a63c8a56c41b913f23e87e5))
* set up rye package manager ([f0eefd7](https://github.com/f-aguzzi/tesi/commit/f0eefd7f704313fca892568b0a72fc2340046c44)), closes [#11](https://github.com/f-aguzzi/tesi/issues/11)


### Docs

* add links to project section pages ([9af2786](https://github.com/f-aguzzi/tesi/commit/9af27863d97731f03a9791f9de1e142e2b78f009)), closes [#9](https://github.com/f-aguzzi/tesi/issues/9)
* first draft of requirements specification ([5d1b8c3](https://github.com/f-aguzzi/tesi/commit/5d1b8c34feeb8e57b68e5a9afb3c03ca7e2188ab))
* updated package name in examples ([33f051f](https://github.com/f-aguzzi/tesi/commit/33f051f2e7b13e4c1126235884f3afc83fbcc31c))


### Refactor

* **svm:** added proper kernel validation ([414cda8](https://github.com/f-aguzzi/tesi/commit/414cda8769e6ae886cda3994bf014eccaebfa0ad)), closes [#8](https://github.com/f-aguzzi/tesi/issues/8)
* made project structure PEP-compliant ([b81e925](https://github.com/f-aguzzi/tesi/commit/b81e925df9bcb31977977e422478292bd6d38199))
* upgrade pylint score ([d80e630](https://github.com/f-aguzzi/tesi/commit/d80e630f785d29f7b54bd65794c096bf0723a592))
