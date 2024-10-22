## [3.1.0](https://github.com/f-aguzzi/tesi/compare/v3.0.0...v3.1.0) (2024-06-29)


### Features

* **DF:** add direct file blob import ([6ea358c](https://github.com/f-aguzzi/tesi/commit/6ea358c99b612fdd2bc79fb7de62cdb85bbf8d1c))
* **DF:** add file-like input capabilities ([e5c707b](https://github.com/f-aguzzi/tesi/commit/e5c707bd5897f363a831cb21ae7d81fb0699c3c7))
* add support for BytesIO inputs ([bab82e8](https://github.com/f-aguzzi/tesi/commit/bab82e8cfc208062a66dee871f28ca32835c951d))


### Docs

* fix broken links in cookbook and documentation ([2353ba9](https://github.com/f-aguzzi/tesi/commit/2353ba928c155a9abf2ff7ba416440e9fe1668f9))


### CI

* **release:** 3.1.0-beta.1 [skip ci] ([673782b](https://github.com/f-aguzzi/tesi/commit/673782bb8543504177d5f8124872eb33310cc889))
* **release:** 3.1.0-beta.2 [skip ci] ([3d8e6da](https://github.com/f-aguzzi/tesi/commit/3d8e6da7eb9beba5fe99c5dc98de04b5f936da99))
* **release:** 3.1.0-beta.3 [skip ci] ([fa0c5b4](https://github.com/f-aguzzi/tesi/commit/fa0c5b44e431edcf1f6964e4671390ceb875a1e1))

## [3.1.0-beta.3](https://github.com/f-aguzzi/tesi/compare/v3.1.0-beta.2...v3.1.0-beta.3) (2024-06-29)


### Features

* **DF:** add direct file blob import ([6ea358c](https://github.com/f-aguzzi/tesi/commit/6ea358c99b612fdd2bc79fb7de62cdb85bbf8d1c))

## [3.1.0-beta.2](https://github.com/f-aguzzi/tesi/compare/v3.1.0-beta.1...v3.1.0-beta.2) (2024-06-29)


### Features

* add support for BytesIO inputs ([bab82e8](https://github.com/f-aguzzi/tesi/commit/bab82e8cfc208062a66dee871f28ca32835c951d))

## [3.1.0-beta.1](https://github.com/f-aguzzi/tesi/compare/v3.0.0...v3.1.0-beta.1) (2024-06-29)


### Features

* **DF:** add file-like input capabilities ([e5c707b](https://github.com/f-aguzzi/tesi/commit/e5c707bd5897f363a831cb21ae7d81fb0699c3c7))


### Docs

* fix broken links in cookbook and documentation ([2353ba9](https://github.com/f-aguzzi/tesi/commit/2353ba928c155a9abf2ff7ba416440e9fe1668f9))

## [3.0.0](https://github.com/f-aguzzi/tesi/compare/v2.5.1...v3.0.0) (2024-06-27)


### ⚠ BREAKING CHANGES

* substitute GraphMode enum with string in API
* **PLSDA:** PLSDA is now also a reducer
* give train() function to BaseActionClass and children

### Features

* feature number autoselection in PLSDA and LDA ([a4f8983](https://github.com/f-aguzzi/tesi/commit/a4f89833fd69f796e0fcad61f745faf77b53c85e))
* **DF:** mid-level data fusion support ([45a3ea4](https://github.com/f-aguzzi/tesi/commit/45a3ea46e80920a56b5f39a2c73b85c5729e0585))
* **DF:** outer matrix multiplication data fusion ([5415a6f](https://github.com/f-aguzzi/tesi/commit/5415a6ff98acc9c395069c9997d3ce23666ab12f))
* **PLSDA:** PLSDA is now also a reducer ([cf67a1a](https://github.com/f-aguzzi/tesi/commit/cf67a1a9366c046e49ce2683e9830d793ab03fa5))
* substitute GraphMode enum with string in API ([34068a4](https://github.com/f-aguzzi/tesi/commit/34068a4c4a5a0213712ae6ee99793dd807d612f9))


### Bug Fixes

* (hoping it will work) remove double dependency ([f4b7cb4](https://github.com/f-aguzzi/tesi/commit/f4b7cb4e29320fd242935945447d6f01c5e93015))
* base-level imports ([8143f74](https://github.com/f-aguzzi/tesi/commit/8143f74698cabd77e70e9f11c754b74ef3d677d5))
* **PCA:** component autoselect issues ([f827b2d](https://github.com/f-aguzzi/tesi/commit/f827b2d2fd835b29a104c7f3527b62a52eb4a671))
* **LDA, BaseReducer:** components bug ([0f87962](https://github.com/f-aguzzi/tesi/commit/0f879621786c7eddfd04c3b6fbaceb297d650800))
* downgrade python to version compatible with Colab ([292d782](https://github.com/f-aguzzi/tesi/commit/292d78249b8a0a4b9b7e32ee3b05ffa04ad2cf5a))
* downgrade scikit-learn ([ad9af1e](https://github.com/f-aguzzi/tesi/commit/ad9af1efa8d6893be89e17f1a81b4795fc3a9530))
* downgrade scipy (I'm desperate, please work) ([62b8ef5](https://github.com/f-aguzzi/tesi/commit/62b8ef5ccbf5aba6051e067756f4722bd15df7cc))
* **DF:** indexing issues when concatenating ([6b29b45](https://github.com/f-aguzzi/tesi/commit/6b29b457d5ca88bfc3ba934cfc936e54f1f7b97a))
* **tests:** KNN and PLSDA test update ([858f560](https://github.com/f-aguzzi/tesi/commit/858f56029cc16fe25795a16997d0d2c28be79ba1))
* last attempt ([7973dc7](https://github.com/f-aguzzi/tesi/commit/7973dc74067da56ac437510aead3c887900a7cc4))
* module exports ([f302243](https://github.com/f-aguzzi/tesi/commit/f302243d4b24c291061a4a0d52ebaed6b36a1d42))
* revert to original 2.5 requirements ([63021c2](https://github.com/f-aguzzi/tesi/commit/63021c2f4361400dd1a2c4ade43691fc63f6def3))
* third round of import debugging ([6d2ad44](https://github.com/f-aguzzi/tesi/commit/6d2ad448016d78c6fc34319ec4386f6bc921425a))
* **DF:** unidimensional time series graphing bug ([a8d5132](https://github.com/f-aguzzi/tesi/commit/a8d5132f237c926fbd084aaa925bf4d38b7e5d7f))
* upgrade numpy to non-devtools version ([9c28adc](https://github.com/f-aguzzi/tesi/commit/9c28adcd30e6b62b83a6372662eacc20f17f3eab))
* upgrade package versions ([d88c87c](https://github.com/f-aguzzi/tesi/commit/d88c87c921775ed5f57ce7c9136fda5974169420))
* upgrade pandas ([0a7d627](https://github.com/f-aguzzi/tesi/commit/0a7d627ccb2d59fde50df4656725f9c568619571))
* wrong import in init file ([726ab66](https://github.com/f-aguzzi/tesi/commit/726ab661060ed369cc532c2a82ea50ba8d9a9653))


### chore

* add version 3.0.0 to docs ([d7da7b7](https://github.com/f-aguzzi/tesi/commit/d7da7b7e707a241fddb141a0a599404da26c24eb))
* make src PEP-compliant ([24e8513](https://github.com/f-aguzzi/tesi/commit/24e8513358ea48b682108eb4a2346f95fede4d1d))
* update CI scripts ([264b153](https://github.com/f-aguzzi/tesi/commit/264b153e5e0f1ca7055e97899e52a93de7f89f81))
* upgrade all examples and case studies ([c084b78](https://github.com/f-aguzzi/tesi/commit/c084b78e8bd9e71e46b080491a39121e4848e651))
* upgrade dependencies ([5657251](https://github.com/f-aguzzi/tesi/commit/5657251e1c2d9b407159c006613bdcb2f6c470c4))


### Docs

* **DF:** mid-level data fusion case study ([f9e3431](https://github.com/f-aguzzi/tesi/commit/f9e343108f4e1023e269c36fff8503fb20cda96f))
* new case study ([35cf415](https://github.com/f-aguzzi/tesi/commit/35cf4158efeec9da7d083f891fbba8f77cf01084))


### Refactor

* give train() function to BaseActionClass and children ([2e836bc](https://github.com/f-aguzzi/tesi/commit/2e836bcb2ed7034873d8bf5cb8b61917ab08303c))
* **DF:** mid-level data fusion overhaul ([b6ba68b](https://github.com/f-aguzzi/tesi/commit/b6ba68bbc0ab25f653f57266e4590e76a8750e85))


### CI

* **release:** 3.0.0-beta.1 [skip ci] ([b9c8cc1](https://github.com/f-aguzzi/tesi/commit/b9c8cc1d43485357a115849c4099ecf20b2cbae0))
* **release:** 3.0.0-beta.10 [skip ci] ([49676d9](https://github.com/f-aguzzi/tesi/commit/49676d912e7e771890e11e3661f59b8c40009b32))
* **release:** 3.0.0-beta.11 [skip ci] ([a85ed04](https://github.com/f-aguzzi/tesi/commit/a85ed045fd01dbd5c600a2c2d9b3cb53936ee91b))
* **release:** 3.0.0-beta.12 [skip ci] ([95b4670](https://github.com/f-aguzzi/tesi/commit/95b4670b9a2cbe13e37c6998d7798236f554df2b))
* **release:** 3.0.0-beta.13 [skip ci] ([e03bfa6](https://github.com/f-aguzzi/tesi/commit/e03bfa60e66190c6ba910e6ca44f6234d6d6f8a5))
* **release:** 3.0.0-beta.14 [skip ci] ([4431802](https://github.com/f-aguzzi/tesi/commit/4431802ca9248e15b2b36e4928e2e0536ecc15b3))
* **release:** 3.0.0-beta.15 [skip ci] ([19253d5](https://github.com/f-aguzzi/tesi/commit/19253d5f17efb92c8f06e5ceeb03d3d47cb28141))
* **release:** 3.0.0-beta.16 [skip ci] ([a221ad7](https://github.com/f-aguzzi/tesi/commit/a221ad75580437e94ee9973d5483aeb011ffae57))
* **release:** 3.0.0-beta.17 [skip ci] ([62146a9](https://github.com/f-aguzzi/tesi/commit/62146a962b18502bb0d02de0917520b9d01040a7))
* **release:** 3.0.0-beta.18 [skip ci] ([153f7dd](https://github.com/f-aguzzi/tesi/commit/153f7dd61f66d826223aa71bdd9a33ad246c2025))
* **release:** 3.0.0-beta.2 [skip ci] ([621a2bf](https://github.com/f-aguzzi/tesi/commit/621a2bf52b37a540e5e3d2eb1d089d5a46d82427))
* **release:** 3.0.0-beta.3 [skip ci] ([8f486b6](https://github.com/f-aguzzi/tesi/commit/8f486b6dfd326488feb42281579d1426f505a97a))
* **release:** 3.0.0-beta.4 [skip ci] ([48f3bf9](https://github.com/f-aguzzi/tesi/commit/48f3bf9a00eb461df2fc49168dc68d838836bf84))
* **release:** 3.0.0-beta.5 [skip ci] ([1d67f76](https://github.com/f-aguzzi/tesi/commit/1d67f7614aa515e135b77515b6eddfa8e259050d))
* **release:** 3.0.0-beta.6 [skip ci] ([fe6e404](https://github.com/f-aguzzi/tesi/commit/fe6e4049219fc94df35a198f0f1675e916e7a111))
* **release:** 3.0.0-beta.7 [skip ci] ([1c3ef74](https://github.com/f-aguzzi/tesi/commit/1c3ef742dc736c18cb3cba8daa4727d47159ef9c))
* **release:** 3.0.0-beta.8 [skip ci] ([b206709](https://github.com/f-aguzzi/tesi/commit/b20670995cd906e7bcc6fe2f425df2e0628db669))
* **release:** 3.0.0-beta.9 [skip ci] ([ff9fe0e](https://github.com/f-aguzzi/tesi/commit/ff9fe0ee160b8fc81e6441f2e5a54ae52a3ce7ca))

## [3.0.0-beta.18](https://github.com/f-aguzzi/tesi/compare/v3.0.0-beta.17...v3.0.0-beta.18) (2024-06-26)


### Bug Fixes

* upgrade pandas ([0a7d627](https://github.com/f-aguzzi/tesi/commit/0a7d627ccb2d59fde50df4656725f9c568619571))

## [3.0.0-beta.17](https://github.com/f-aguzzi/tesi/compare/v3.0.0-beta.16...v3.0.0-beta.17) (2024-06-26)


### Bug Fixes

* upgrade numpy to non-devtools version ([9c28adc](https://github.com/f-aguzzi/tesi/commit/9c28adcd30e6b62b83a6372662eacc20f17f3eab))

## [3.0.0-beta.16](https://github.com/f-aguzzi/tesi/compare/v3.0.0-beta.15...v3.0.0-beta.16) (2024-06-26)

## [3.0.0-beta.15](https://github.com/f-aguzzi/tesi/compare/v3.0.0-beta.14...v3.0.0-beta.15) (2024-06-26)


### Bug Fixes

* please work. I need this to work. ([43199e9](https://github.com/f-aguzzi/tesi/commit/43199e971ad7bee1808cab9040427bc2fec2761e))

## [3.0.0-beta.14](https://github.com/f-aguzzi/tesi/compare/v3.0.0-beta.13...v3.0.0-beta.14) (2024-06-26)


### Bug Fixes

* revert to original 2.5 requirements ([63021c2](https://github.com/f-aguzzi/tesi/commit/63021c2f4361400dd1a2c4ade43691fc63f6def3))

## [3.0.0-beta.13](https://github.com/f-aguzzi/tesi/compare/v3.0.0-beta.12...v3.0.0-beta.13) (2024-06-26)


### Bug Fixes

* **base:** remove bug-causing BaseEstimator check ([4e9d3b9](https://github.com/f-aguzzi/tesi/commit/4e9d3b9eed9c5fc5f208d5fab82a84225cf03b6b))

## [3.0.0-beta.12](https://github.com/f-aguzzi/tesi/compare/v3.0.0-beta.11...v3.0.0-beta.12) (2024-06-26)


### Bug Fixes

* downgrade scikit-learn ([ad9af1e](https://github.com/f-aguzzi/tesi/commit/ad9af1efa8d6893be89e17f1a81b4795fc3a9530))

## [3.0.0-beta.11](https://github.com/f-aguzzi/tesi/compare/v3.0.0-beta.10...v3.0.0-beta.11) (2024-06-26)


### Bug Fixes

* wrong import in init file ([726ab66](https://github.com/f-aguzzi/tesi/commit/726ab661060ed369cc532c2a82ea50ba8d9a9653))

## [3.0.0-beta.10](https://github.com/f-aguzzi/tesi/compare/v3.0.0-beta.9...v3.0.0-beta.10) (2024-06-26)


### Bug Fixes

* last attempt ([7973dc7](https://github.com/f-aguzzi/tesi/commit/7973dc74067da56ac437510aead3c887900a7cc4))

## [3.0.0-beta.9](https://github.com/f-aguzzi/tesi/compare/v3.0.0-beta.8...v3.0.0-beta.9) (2024-06-26)


### Bug Fixes

* (hoping it will work) remove double dependency ([f4b7cb4](https://github.com/f-aguzzi/tesi/commit/f4b7cb4e29320fd242935945447d6f01c5e93015))

## [3.0.0-beta.8](https://github.com/f-aguzzi/tesi/compare/v3.0.0-beta.7...v3.0.0-beta.8) (2024-06-26)


### Bug Fixes

* downgrade scipy (I'm desperate, please work) ([62b8ef5](https://github.com/f-aguzzi/tesi/commit/62b8ef5ccbf5aba6051e067756f4722bd15df7cc))

## [3.0.0-beta.7](https://github.com/f-aguzzi/tesi/compare/v3.0.0-beta.6...v3.0.0-beta.7) (2024-06-26)


### Bug Fixes

* downgrade python to version compatible with Colab ([292d782](https://github.com/f-aguzzi/tesi/commit/292d78249b8a0a4b9b7e32ee3b05ffa04ad2cf5a))

## [3.0.0-beta.6](https://github.com/f-aguzzi/tesi/compare/v3.0.0-beta.5...v3.0.0-beta.6) (2024-06-26)


### Bug Fixes

* third round of import debugging ([6d2ad44](https://github.com/f-aguzzi/tesi/commit/6d2ad448016d78c6fc34319ec4386f6bc921425a))

## [3.0.0-beta.5](https://github.com/f-aguzzi/tesi/compare/v3.0.0-beta.4...v3.0.0-beta.5) (2024-06-26)


### Bug Fixes

* base-level imports ([8143f74](https://github.com/f-aguzzi/tesi/commit/8143f74698cabd77e70e9f11c754b74ef3d677d5))


### chore

* update CI scripts ([264b153](https://github.com/f-aguzzi/tesi/commit/264b153e5e0f1ca7055e97899e52a93de7f89f81))

## [3.0.0-beta.4](https://github.com/f-aguzzi/tesi/compare/v3.0.0-beta.3...v3.0.0-beta.4) (2024-06-26)


### Bug Fixes

* module exports ([f302243](https://github.com/f-aguzzi/tesi/commit/f302243d4b24c291061a4a0d52ebaed6b36a1d42))

## [3.0.0-beta.3](https://github.com/f-aguzzi/tesi/compare/v3.0.0-beta.2...v3.0.0-beta.3) (2024-06-26)


### Bug Fixes

* **DF:** unidimensional time series graphing bug ([a8d5132](https://github.com/f-aguzzi/tesi/commit/a8d5132f237c926fbd084aaa925bf4d38b7e5d7f))


### chore

* make src PEP-compliant ([24e8513](https://github.com/f-aguzzi/tesi/commit/24e8513358ea48b682108eb4a2346f95fede4d1d))
* upgrade dependencies ([5657251](https://github.com/f-aguzzi/tesi/commit/5657251e1c2d9b407159c006613bdcb2f6c470c4))

## [3.0.0-beta.2](https://github.com/f-aguzzi/tesi/compare/v3.0.0-beta.1...v3.0.0-beta.2) (2024-06-25)


### Bug Fixes

* upgrade package versions ([d88c87c](https://github.com/f-aguzzi/tesi/commit/d88c87c921775ed5f57ce7c9136fda5974169420))

## [3.0.0-beta.1](https://github.com/f-aguzzi/tesi/compare/v2.5.0...v3.0.0-beta.1) (2024-06-24)


### ⚠ BREAKING CHANGES

* substitute GraphMode enum with string in API
* **PLSDA:** PLSDA is now also a reducer
* give train() function to BaseActionClass and children

### Features

* feature number autoselection in PLSDA and LDA ([a4f8983](https://github.com/f-aguzzi/tesi/commit/a4f89833fd69f796e0fcad61f745faf77b53c85e))
* **DF:** mid-level data fusion support ([45a3ea4](https://github.com/f-aguzzi/tesi/commit/45a3ea46e80920a56b5f39a2c73b85c5729e0585))
* **DF:** outer matrix multiplication data fusion ([5415a6f](https://github.com/f-aguzzi/tesi/commit/5415a6ff98acc9c395069c9997d3ce23666ab12f))
* **PLSDA:** PLSDA is now also a reducer ([cf67a1a](https://github.com/f-aguzzi/tesi/commit/cf67a1a9366c046e49ce2683e9830d793ab03fa5))
* substitute GraphMode enum with string in API ([34068a4](https://github.com/f-aguzzi/tesi/commit/34068a4c4a5a0213712ae6ee99793dd807d612f9))


### Bug Fixes

* **PCA:** component autoselect issues ([f827b2d](https://github.com/f-aguzzi/tesi/commit/f827b2d2fd835b29a104c7f3527b62a52eb4a671))
* **LDA, BaseReducer:** components bug ([0f87962](https://github.com/f-aguzzi/tesi/commit/0f879621786c7eddfd04c3b6fbaceb297d650800))
* **DF:** indexing issues when concatenating ([6b29b45](https://github.com/f-aguzzi/tesi/commit/6b29b457d5ca88bfc3ba934cfc936e54f1f7b97a))
* **tests:** KNN and PLSDA test update ([858f560](https://github.com/f-aguzzi/tesi/commit/858f56029cc16fe25795a16997d0d2c28be79ba1))


### Docs

* **DF:** mid-level data fusion case study ([f9e3431](https://github.com/f-aguzzi/tesi/commit/f9e343108f4e1023e269c36fff8503fb20cda96f))
* new case study ([35cf415](https://github.com/f-aguzzi/tesi/commit/35cf4158efeec9da7d083f891fbba8f77cf01084))


### Refactor

* give train() function to BaseActionClass and children ([2e836bc](https://github.com/f-aguzzi/tesi/commit/2e836bcb2ed7034873d8bf5cb8b61917ab08303c))
* **DF:** mid-level data fusion overhaul ([b6ba68b](https://github.com/f-aguzzi/tesi/commit/b6ba68bbc0ab25f653f57266e4590e76a8750e85))

## [2.5.1](https://github.com/f-aguzzi/tesi/compare/v2.5.0...v2.5.1) (2024-06-17)

### Bug Fixes

* **LLDF:** format-specific reader in y column import ([84c6b5e](https://github.com/f-aguzzi/tesi/commit/84c6b5ee777a1549dfc067d80c131ff610865f61))


## [2.5.0](https://github.com/f-aguzzi/tesi/compare/v2.4.0...v2.5.0) (2024-06-13)


### Features

* **base:** added BaseActionClass as root class ([4f0bac8](https://github.com/f-aguzzi/tesi/commit/4f0bac831f6ca215212f6c801b01483ef2d0e5cc))
* LDA and PCA inherit from BaseReducer ([7b797bd](https://github.com/f-aguzzi/tesi/commit/7b797bdfb00404b90fdeaf4178085f2d2bdb9c34))


### Bug Fixes

* **pca:** field and property issues ([91cefd3](https://github.com/f-aguzzi/tesi/commit/91cefd3d66475d13ed990ed2911014cc866e2f8d))
* **base:** inheritance settings (2) ([103040c](https://github.com/f-aguzzi/tesi/commit/103040c940ba884debaf8fdc2239d3dee0e76ab2))
* **base:** settings inheritance ([8a14a00](https://github.com/f-aguzzi/tesi/commit/8a14a0036bf3791deda182ec0f3aa618806f180d))
* **base:** third round of inheritance fixes ([c3b1bbb](https://github.com/f-aguzzi/tesi/commit/c3b1bbb36c7c150525a6d9d0c87f863291ad397e))
* **BaseActionClass:** trailing commas creating unwanted tuple ([1b057ab](https://github.com/f-aguzzi/tesi/commit/1b057abb23710c0aef8f67875411d63e47a61036))


### chore

* **styling:** increase PEP compliance ([1ea3546](https://github.com/f-aguzzi/tesi/commit/1ea354688415f1f4f5c8398365a0757e3b665dc7))
* **docs, examples:** update for version 2.5.0 ([4c6b0d3](https://github.com/f-aguzzi/tesi/commit/4c6b0d392ca82d5eb4079780dbb303d7ffc43236)), closes [#32](https://github.com/f-aguzzi/tesi/issues/32)
* **docs:** upgrade to version 2.5.0 ([387499f](https://github.com/f-aguzzi/tesi/commit/387499f5add4ceae62d07891ffd531406607cdaf))


### Docs

* **blog:** add blog posts for new releases ([f8461d8](https://github.com/f-aguzzi/tesi/commit/f8461d8747a5a80c27b8e8c94d245b19fc7e22ec))
* finish first case study ([21fcb01](https://github.com/f-aguzzi/tesi/commit/21fcb014b8b510fe7718e1443a1daad0afd09e0e))
* fix naming error ([78d59e4](https://github.com/f-aguzzi/tesi/commit/78d59e4e5467015d50fcd02cb75a622f89bd80e6))


### CI

* **release:** 2.5.0-beta.1 [skip ci] ([5578065](https://github.com/f-aguzzi/tesi/commit/55780657ee054384ddf7de5551b653ecd1a0d5c3))
* **release:** 2.5.0-beta.2 [skip ci] ([8a5334d](https://github.com/f-aguzzi/tesi/commit/8a5334da0098180aa5e63017c85b28a50ae0a295))
* **release:** 2.5.0-beta.3 [skip ci] ([6706948](https://github.com/f-aguzzi/tesi/commit/67069489eef56f124a8da7980aad4f35978bcdae))
* **release:** 2.5.0-beta.4 [skip ci] ([61d1a32](https://github.com/f-aguzzi/tesi/commit/61d1a32ca9226409405351b90fec4087d88d6b44))
* **release:** 2.5.0-beta.5 [skip ci] ([6f69537](https://github.com/f-aguzzi/tesi/commit/6f69537d621f8a726198bf3193efeb45866b9c03))
* **release:** 2.5.0-beta.6 [skip ci] ([f732442](https://github.com/f-aguzzi/tesi/commit/f7324424fb6b980f1dd99fe02b3a9de2acd8c682))

## [2.5.0-beta.6](https://github.com/f-aguzzi/tesi/compare/v2.5.0-beta.5...v2.5.0-beta.6) (2024-06-12)


### Bug Fixes

* **pca:** field and property issues ([91cefd3](https://github.com/f-aguzzi/tesi/commit/91cefd3d66475d13ed990ed2911014cc866e2f8d))

## [2.5.0-beta.5](https://github.com/f-aguzzi/tesi/compare/v2.5.0-beta.4...v2.5.0-beta.5) (2024-06-12)


### Bug Fixes

* **BaseActionClass:** trailing commas creating unwanted tuple ([1b057ab](https://github.com/f-aguzzi/tesi/commit/1b057abb23710c0aef8f67875411d63e47a61036))

## [2.5.0-beta.4](https://github.com/f-aguzzi/tesi/compare/v2.5.0-beta.3...v2.5.0-beta.4) (2024-06-12)


### Bug Fixes

* **base:** third round of inheritance fixes ([c3b1bbb](https://github.com/f-aguzzi/tesi/commit/c3b1bbb36c7c150525a6d9d0c87f863291ad397e))

## [2.5.0-beta.3](https://github.com/f-aguzzi/tesi/compare/v2.5.0-beta.2...v2.5.0-beta.3) (2024-06-12)


### Bug Fixes

* **base:** inheritance settings (2) ([103040c](https://github.com/f-aguzzi/tesi/commit/103040c940ba884debaf8fdc2239d3dee0e76ab2))

## [2.5.0-beta.2](https://github.com/f-aguzzi/tesi/compare/v2.5.0-beta.1...v2.5.0-beta.2) (2024-06-12)


### Bug Fixes

* **base:** settings inheritance ([8a14a00](https://github.com/f-aguzzi/tesi/commit/8a14a0036bf3791deda182ec0f3aa618806f180d))

## [2.5.0-beta.1](https://github.com/f-aguzzi/tesi/compare/v2.4.0...v2.5.0-beta.1) (2024-06-12)


### Features

* **base:** added BaseActionClass as root class ([4f0bac8](https://github.com/f-aguzzi/tesi/commit/4f0bac831f6ca215212f6c801b01483ef2d0e5cc))
* LDA and PCA inherit from BaseReducer ([7b797bd](https://github.com/f-aguzzi/tesi/commit/7b797bdfb00404b90fdeaf4178085f2d2bdb9c34))


### chore

* **docs:** upgrade to version 2.5.0 ([387499f](https://github.com/f-aguzzi/tesi/commit/387499f5add4ceae62d07891ffd531406607cdaf))


### Docs

* finish first case study ([21fcb01](https://github.com/f-aguzzi/tesi/commit/21fcb014b8b510fe7718e1443a1daad0afd09e0e))

## [2.4.0](https://github.com/f-aguzzi/tesi/compare/v2.3.0...v2.4.0) (2024-06-11)


### Features

* add from_file classmethod to BaseClassifier ([9478f88](https://github.com/f-aguzzi/tesi/commit/9478f88dbf58df1c5e06fbf1a996b936b8b174f9))
* **PCA:** added reduce method ([1ad418e](https://github.com/f-aguzzi/tesi/commit/1ad418eec712522038dab118744c60a0dbf8f47f))
* **PCA:** model import and export ([15e13f1](https://github.com/f-aguzzi/tesi/commit/15e13f13897073f79373924fb4658e3ecb590085))
* PCA rescaled_data property ([9eb9301](https://github.com/f-aguzzi/tesi/commit/9eb93015e4fa936f93de46cf25c8de6d7898440e))
* **LLDF:** print table name in graphs ([1d78181](https://github.com/f-aguzzi/tesi/commit/1d78181a7f066e63c8eebcbcfee019a076882fc6))
* **BaseDataModel:** subscript sample selection ([0830397](https://github.com/f-aguzzi/tesi/commit/08303978b5773f16fbbd98c30b7751959d759558))


### Bug Fixes

* **LR:** add special case for binary classifiers ([8da46b7](https://github.com/f-aguzzi/tesi/commit/8da46b7ecb5f2708fff9d6088eb484ce0ad13f6f))
* **PCA:** conditions of reduce exception raising ([1f74220](https://github.com/f-aguzzi/tesi/commit/1f74220039b0f59374f568ea5744dc3728a28a13))
* error in condition in extended split tests ([5b56d15](https://github.com/f-aguzzi/tesi/commit/5b56d15787e95830dcc3937d21af5b8e93af8219))
* **LLDF:** graph printing issues ([6eb9fba](https://github.com/f-aguzzi/tesi/commit/6eb9fba431339e430145d1d3dbc54ee9d6f6a802))
* **LLDF:** import column names checking ([f51b11c](https://github.com/f-aguzzi/tesi/commit/f51b11c9981f9f7a26d688ab1954003e8be443a6))
* **changelog:** realign versions ([24d74bf](https://github.com/f-aguzzi/tesi/commit/24d74bf7f8cb72f64cfd9732b0f7160b063d1a30))
* **gitignore:** remove duplicates ([4442fb6](https://github.com/f-aguzzi/tesi/commit/4442fb674c25640e405991ef71022cd4071743b6))
* **tests:** test case for BaseDataModel import/export ([0817547](https://github.com/f-aguzzi/tesi/commit/081754777e0b9be2a7ffe9b86b403a4538a682e1))
* **pyproject:** update version ([4c2824f](https://github.com/f-aguzzi/tesi/commit/4c2824fa275cf21e4db339082238fd346b8fb79f))
* **LLDF:** wrong data concatenation ([9bb5f93](https://github.com/f-aguzzi/tesi/commit/9bb5f9346d4ee19b11deaaf7567e4dd9538c3fd7))


### chore

* **docs:** upgrade to version 2.4.0 ([b296bbc](https://github.com/f-aguzzi/tesi/commit/b296bbc18506e6d058bf44e3de7eefc2ca416bfe))


### Docs

* updated case studies ([f838c2e](https://github.com/f-aguzzi/tesi/commit/f838c2e8d095f07e8c7f64e3776f072be6293728))


### CI

* **release:** 2.3.0-beta.10 [skip ci] ([ae1b35e](https://github.com/f-aguzzi/tesi/commit/ae1b35e0f5c8e5c6b6668792b4bbf019563b5c41))
* **release:** 2.3.0-beta.11 [skip ci] ([d3b07cb](https://github.com/f-aguzzi/tesi/commit/d3b07cb18576794df9c0c74770adccfa65b6d52f))
* **release:** 2.3.0-beta.12 [skip ci] ([7c653ac](https://github.com/f-aguzzi/tesi/commit/7c653ac50ff5f22cc00022b03004e4d6946c6e3b))
* **release:** 2.3.0-beta.13 [skip ci] ([2baa4ea](https://github.com/f-aguzzi/tesi/commit/2baa4eab7cfc3ae8c09b8a4e00e27ece23aff90b))
* **release:** 2.3.0-beta.14 [skip ci] ([84028f8](https://github.com/f-aguzzi/tesi/commit/84028f81f6e2cd4d50cd1f2d69ecc72c7d7edfe5))
* **release:** 2.3.0-beta.4 [skip ci] ([45a03cf](https://github.com/f-aguzzi/tesi/commit/45a03cf5a791a40a4a4701dca5c49d75b11c4239))
* **release:** 2.3.0-beta.5 [skip ci] ([c3a296b](https://github.com/f-aguzzi/tesi/commit/c3a296ba41d33ede5706e0454b135a21969682da))
* **release:** 2.3.0-beta.6 [skip ci] ([0266be5](https://github.com/f-aguzzi/tesi/commit/0266be5e348a90768a7dbe383100998516632852))
* **release:** 2.3.0-beta.7 [skip ci] ([6a6568d](https://github.com/f-aguzzi/tesi/commit/6a6568d77e951ddf5f3f4a0589b5b9ee70b4cc21))
* **release:** 2.3.0-beta.8 [skip ci] ([65d0446](https://github.com/f-aguzzi/tesi/commit/65d04462323be399b908391b95b41b7f6ecf85fc))
* **release:** 2.3.0-beta.9 [skip ci] ([dff1da7](https://github.com/f-aguzzi/tesi/commit/dff1da7f77a1fb6620d9efd1ba0dde102bf7c5d0))
* **release:** 2.4.0-beta.1 [skip ci] ([d4ebd2c](https://github.com/f-aguzzi/tesi/commit/d4ebd2c5b3af5e7a59d9fe7c8ed6fa65e407f728))

## [2.4.0-beta.1](https://github.com/f-aguzzi/tesi/compare/v2.3.0...v2.4.0-beta.1) (2024-06-11)


### Features

* add from_file classmethod to BaseClassifier ([9478f88](https://github.com/f-aguzzi/tesi/commit/9478f88dbf58df1c5e06fbf1a996b936b8b174f9))
* **PCA:** added reduce method ([1ad418e](https://github.com/f-aguzzi/tesi/commit/1ad418eec712522038dab118744c60a0dbf8f47f))
* **PCA:** model import and export ([15e13f1](https://github.com/f-aguzzi/tesi/commit/15e13f13897073f79373924fb4658e3ecb590085))
* PCA rescaled_data property ([9eb9301](https://github.com/f-aguzzi/tesi/commit/9eb93015e4fa936f93de46cf25c8de6d7898440e))
* **LLDF:** print table name in graphs ([1d78181](https://github.com/f-aguzzi/tesi/commit/1d78181a7f066e63c8eebcbcfee019a076882fc6))
* **BaseDataModel:** subscript sample selection ([0830397](https://github.com/f-aguzzi/tesi/commit/08303978b5773f16fbbd98c30b7751959d759558))


### Bug Fixes

* **LR:** add special case for binary classifiers ([8da46b7](https://github.com/f-aguzzi/tesi/commit/8da46b7ecb5f2708fff9d6088eb484ce0ad13f6f))
* **PCA:** conditions of reduce exception raising ([1f74220](https://github.com/f-aguzzi/tesi/commit/1f74220039b0f59374f568ea5744dc3728a28a13))
* error in condition in extended split tests ([5b56d15](https://github.com/f-aguzzi/tesi/commit/5b56d15787e95830dcc3937d21af5b8e93af8219))
* **LLDF:** graph printing issues ([6eb9fba](https://github.com/f-aguzzi/tesi/commit/6eb9fba431339e430145d1d3dbc54ee9d6f6a802))
* **LLDF:** import column names checking ([f51b11c](https://github.com/f-aguzzi/tesi/commit/f51b11c9981f9f7a26d688ab1954003e8be443a6))
* **changelog:** realign versions ([24d74bf](https://github.com/f-aguzzi/tesi/commit/24d74bf7f8cb72f64cfd9732b0f7160b063d1a30))
* **gitignore:** remove duplicates ([4442fb6](https://github.com/f-aguzzi/tesi/commit/4442fb674c25640e405991ef71022cd4071743b6))
* **tests:** test case for BaseDataModel import/export ([0817547](https://github.com/f-aguzzi/tesi/commit/081754777e0b9be2a7ffe9b86b403a4538a682e1))
* **pyproject:** update version ([4c2824f](https://github.com/f-aguzzi/tesi/commit/4c2824fa275cf21e4db339082238fd346b8fb79f))
* **LLDF:** wrong data concatenation ([9bb5f93](https://github.com/f-aguzzi/tesi/commit/9bb5f9346d4ee19b11deaaf7567e4dd9538c3fd7))


### chore

* **docs:** upgrade to version 2.4.0 ([b296bbc](https://github.com/f-aguzzi/tesi/commit/b296bbc18506e6d058bf44e3de7eefc2ca416bfe))


### Docs

* updated case studies ([f838c2e](https://github.com/f-aguzzi/tesi/commit/f838c2e8d095f07e8c7f64e3776f072be6293728))


### CI

* **release:** 2.3.0-beta.10 [skip ci] ([ae1b35e](https://github.com/f-aguzzi/tesi/commit/ae1b35e0f5c8e5c6b6668792b4bbf019563b5c41))
* **release:** 2.3.0-beta.11 [skip ci] ([d3b07cb](https://github.com/f-aguzzi/tesi/commit/d3b07cb18576794df9c0c74770adccfa65b6d52f))
* **release:** 2.3.0-beta.12 [skip ci] ([7c653ac](https://github.com/f-aguzzi/tesi/commit/7c653ac50ff5f22cc00022b03004e4d6946c6e3b))
* **release:** 2.3.0-beta.13 [skip ci] ([2baa4ea](https://github.com/f-aguzzi/tesi/commit/2baa4eab7cfc3ae8c09b8a4e00e27ece23aff90b))
* **release:** 2.3.0-beta.14 [skip ci] ([84028f8](https://github.com/f-aguzzi/tesi/commit/84028f81f6e2cd4d50cd1f2d69ecc72c7d7edfe5))
* **release:** 2.3.0-beta.4 [skip ci] ([45a03cf](https://github.com/f-aguzzi/tesi/commit/45a03cf5a791a40a4a4701dca5c49d75b11c4239))
* **release:** 2.3.0-beta.5 [skip ci] ([c3a296b](https://github.com/f-aguzzi/tesi/commit/c3a296ba41d33ede5706e0454b135a21969682da))
* **release:** 2.3.0-beta.6 [skip ci] ([0266be5](https://github.com/f-aguzzi/tesi/commit/0266be5e348a90768a7dbe383100998516632852))
* **release:** 2.3.0-beta.7 [skip ci] ([6a6568d](https://github.com/f-aguzzi/tesi/commit/6a6568d77e951ddf5f3f4a0589b5b9ee70b4cc21))
* **release:** 2.3.0-beta.8 [skip ci] ([65d0446](https://github.com/f-aguzzi/tesi/commit/65d04462323be399b908391b95b41b7f6ecf85fc))
* **release:** 2.3.0-beta.9 [skip ci] ([dff1da7](https://github.com/f-aguzzi/tesi/commit/dff1da7f77a1fb6620d9efd1ba0dde102bf7c5d0))

## [2.4.0-beta.1](https://github.com/f-aguzzi/tesi/compare/v2.3.0-beta.14...v2.4.0-beta.1) (2024-06-11)


### chore

* **ci:** manually fix broken semantic release

## [2.3.0-beta.14](https://github.com/f-aguzzi/tesi/compare/v2.3.0-beta.13...v2.3.0-beta.14) (2024-06-11)


### Bug Fixes

* **gitignore:** remove duplicates ([4442fb6](https://github.com/f-aguzzi/tesi/commit/4442fb674c25640e405991ef71022cd4071743b6))

## [2.3.0-beta.13](https://github.com/f-aguzzi/tesi/compare/v2.3.0-beta.12...v2.3.0-beta.13) (2024-06-11)


### Bug Fixes

* **changelog:** realign versions ([24d74bf](https://github.com/f-aguzzi/tesi/commit/24d74bf7f8cb72f64cfd9732b0f7160b063d1a30))


### chore

* **docs:** upgrade to version 2.4.0 ([b296bbc](https://github.com/f-aguzzi/tesi/commit/b296bbc18506e6d058bf44e3de7eefc2ca416bfe))

## [2.3.0-beta.12](https://github.com/f-aguzzi/tesi/compare/v2.3.0-beta.11...v2.3.0-beta.12) (2024-06-11)


### Bug Fixes

* **tests:** test case for BaseDataModel import/export ([0817547](https://github.com/f-aguzzi/tesi/commit/081754777e0b9be2a7ffe9b86b403a4538a682e1))

## [2.3.0-beta.11](https://github.com/f-aguzzi/tesi/compare/v2.3.0-beta.10...v2.3.0-beta.11) (2024-06-11)


### Features

* **LLDF:** print table name in graphs ([1d78181](https://github.com/f-aguzzi/tesi/commit/1d78181a7f066e63c8eebcbcfee019a076882fc6))


### Bug Fixes

* error in condition in extended split tests ([5b56d15](https://github.com/f-aguzzi/tesi/commit/5b56d15787e95830dcc3937d21af5b8e93af8219))


### Docs

* updated case studies ([f838c2e](https://github.com/f-aguzzi/tesi/commit/f838c2e8d095f07e8c7f64e3776f072be6293728))

## [2.3.0-beta.10](https://github.com/f-aguzzi/tesi/compare/v2.3.0-beta.9...v2.3.0-beta.10) (2024-06-11)


### Features

* **BaseDataModel:** subscript sample selection ([0830397](https://github.com/f-aguzzi/tesi/commit/08303978b5773f16fbbd98c30b7751959d759558))

## [2.3.0-beta.9](https://github.com/f-aguzzi/tesi/compare/v2.3.0-beta.8...v2.3.0-beta.9) (2024-06-11)


### Bug Fixes

* **LR:** add special case for binary classifiers ([8da46b7](https://github.com/f-aguzzi/tesi/commit/8da46b7ecb5f2708fff9d6088eb484ce0ad13f6f))
* **LLDF:** wrong data concatenation ([9bb5f93](https://github.com/f-aguzzi/tesi/commit/9bb5f9346d4ee19b11deaaf7567e4dd9538c3fd7))

## [2.3.0-beta.8](https://github.com/f-aguzzi/tesi/compare/v2.3.0-beta.7...v2.3.0-beta.8) (2024-06-11)


### Bug Fixes

* **LLDF:** graph printing issues ([6eb9fba](https://github.com/f-aguzzi/tesi/commit/6eb9fba431339e430145d1d3dbc54ee9d6f6a802))
* **LLDF:** import column names checking ([f51b11c](https://github.com/f-aguzzi/tesi/commit/f51b11c9981f9f7a26d688ab1954003e8be443a6))

## [2.3.0-beta.7](https://github.com/f-aguzzi/tesi/compare/v2.3.0-beta.6...v2.3.0-beta.7) (2024-06-11)


### Bug Fixes

* **PCA:** conditions of reduce exception raising ([1f74220](https://github.com/f-aguzzi/tesi/commit/1f74220039b0f59374f568ea5744dc3728a28a13))

## [2.3.0-beta.6](https://github.com/f-aguzzi/tesi/compare/v2.3.0-beta.5...v2.3.0-beta.6) (2024-06-11)


### Features

* **PCA:** added reduce method ([1ad418e](https://github.com/f-aguzzi/tesi/commit/1ad418eec712522038dab118744c60a0dbf8f47f))

## [2.3.0-beta.5](https://github.com/f-aguzzi/tesi/compare/v2.3.0-beta.4...v2.3.0-beta.5) (2024-06-11)


### Features

* add from_file classmethod to BaseClassifier ([9478f88](https://github.com/f-aguzzi/tesi/commit/9478f88dbf58df1c5e06fbf1a996b936b8b174f9))
* **PCA:** model import and export ([15e13f1](https://github.com/f-aguzzi/tesi/commit/15e13f13897073f79373924fb4658e3ecb590085))

## [2.3.0-beta.4](https://github.com/f-aguzzi/tesi/compare/v2.3.0-beta.3...v2.3.0-beta.4) (2024-06-11)


### Features

* PCA rescaled_data property ([9eb9301](https://github.com/f-aguzzi/tesi/commit/9eb93015e4fa936f93de46cf25c8de6d7898440e))

## [2.3.0](https://github.com/f-aguzzi/tesi/compare/v2.2.0...v2.3.0) (2024-06-10)


### Features

* added json and csv support for table import/export ([392933a](https://github.com/f-aguzzi/tesi/commit/392933a09d7333e81d99feb6a5b67bd5e30051d4))


### Bug Fixes

* **CI/CD:** conditional workflow run ([74d308b](https://github.com/f-aguzzi/tesi/commit/74d308be2f4c1750e5d6f8bcbda889e895a828fa))
* **lldf:** wrong exception type on export with invalid format ([3842ed9](https://github.com/f-aguzzi/tesi/commit/3842ed9d1f003c19565ef1a4cbd8e5544f6476e4))


### Docs

* version 2.3.0 ([a10d464](https://github.com/f-aguzzi/tesi/commit/a10d46437e5c6d3fe29d3b4fded01e87e352687e))


### CI

* **release:** 2.3.0-beta.1 [skip ci] ([6734667](https://github.com/f-aguzzi/tesi/commit/6734667e583e6194343658f169a771d0ba4981d4))
* **release:** 2.3.0-beta.2 [skip ci] ([0551ea0](https://github.com/f-aguzzi/tesi/commit/0551ea07fe9a8514552e4af09efb030c8d112ffa))
* **release:** 2.3.0-beta.3 [skip ci] ([aa9e280](https://github.com/f-aguzzi/tesi/commit/aa9e2800d1b7d5bdf20d3f0b53e0a04f17f0d8c5))

## [2.3.0-beta.3](https://github.com/f-aguzzi/tesi/compare/v2.3.0-beta.2...v2.3.0-beta.3) (2024-06-08)


### Bug Fixes

* **CI/CD:** conditional workflow run ([74d308b](https://github.com/f-aguzzi/tesi/commit/74d308be2f4c1750e5d6f8bcbda889e895a828fa))

## [2.3.0-beta.2](https://github.com/f-aguzzi/tesi/compare/v2.3.0-beta.1...v2.3.0-beta.2) (2024-06-08)


### Bug Fixes

* **lldf:** wrong exception type on export with invalid format ([3842ed9](https://github.com/f-aguzzi/tesi/commit/3842ed9d1f003c19565ef1a4cbd8e5544f6476e4))

## [2.3.0-beta.1](https://github.com/f-aguzzi/tesi/compare/v2.2.0...v2.3.0-beta.1) (2024-06-08)


### Features

* added json and csv support for table import/export ([392933a](https://github.com/f-aguzzi/tesi/commit/392933a09d7333e81d99feb6a5b67bd5e30051d4))


### Docs

* version 2.3.0 ([a10d464](https://github.com/f-aguzzi/tesi/commit/a10d46437e5c6d3fe29d3b4fded01e87e352687e))

## [2.2.0](https://github.com/f-aguzzi/tesi/compare/v2.1.0...v2.2.0) (2024-06-07)


### Features

* excel import with user-defined schema ([f0d0d74](https://github.com/f-aguzzi/tesi/commit/f0d0d74efa04711d89bafa2082c352f117fd0680))


### Docs

* update to version 2.2.0 ([ebff95d](https://github.com/f-aguzzi/tesi/commit/ebff95d7cf00d7c86d987d113543631acc0a0113))


### CI

* **release:** 2.2.0-beta.1 [skip ci] ([4249066](https://github.com/f-aguzzi/tesi/commit/424906654381225681761d3d62e7bd0ac93d3c79))

## [2.2.0-beta.1](https://github.com/f-aguzzi/tesi/compare/v2.1.0...v2.2.0-beta.1) (2024-06-07)


### Features

* excel import with user-defined schema ([f0d0d74](https://github.com/f-aguzzi/tesi/commit/f0d0d74efa04711d89bafa2082c352f117fd0680))


### Docs

* update to version 2.2.0 ([ebff95d](https://github.com/f-aguzzi/tesi/commit/ebff95d7cf00d7c86d987d113543631acc0a0113))

## [2.1.0](https://github.com/f-aguzzi/tesi/compare/v2.0.0...v2.1.0) (2024-06-07)


### Features

* **import/export:** fully functional file dumping ([e1d0044](https://github.com/f-aguzzi/tesi/commit/e1d004448afd86f4ffa2ed4b87629e6798ef41b2))


### chore

* **license:** add GPLv3 license ([3fdd0b8](https://github.com/f-aguzzi/tesi/commit/3fdd0b87b6587b7413dd36f5101d37a5d712e7d7))
* **docs:** version 2.1.0 ([3601750](https://github.com/f-aguzzi/tesi/commit/3601750fab58414dfe565abb7ecab57630b61a31))


### Docs

* add new information ([be7c262](https://github.com/f-aguzzi/tesi/commit/be7c2624710d6dbf4f0d320e451e5001853560cc))


### CI

* **release:** 2.1.0-beta.1 [skip ci] ([39c5542](https://github.com/f-aguzzi/tesi/commit/39c55420774090231db53ccbacf52ffbbc53009e))

## [2.1.0-beta.1](https://github.com/f-aguzzi/tesi/compare/v2.0.0...v2.1.0-beta.1) (2024-06-05)


### Features

* **import/export:** fully functional file dumping ([e1d0044](https://github.com/f-aguzzi/tesi/commit/e1d004448afd86f4ffa2ed4b87629e6798ef41b2))


### chore

* **license:** add GPLv3 license ([3fdd0b8](https://github.com/f-aguzzi/tesi/commit/3fdd0b87b6587b7413dd36f5101d37a5d712e7d7))

## [2.0.0](https://github.com/f-aguzzi/tesi/compare/v1.2.0...v2.0.0) (2024-06-04)


### ⚠ BREAKING CHANGES

* added base class for classifiers, models, settings

### Features

* added base class for classifiers, models, settings ([4af5d47](https://github.com/f-aguzzi/tesi/commit/4af5d4778d28021dcd2e23f00fc5810ae178769d))
* **LDA:** autodetect components from PCADataModel ([a59cd54](https://github.com/f-aguzzi/tesi/commit/a59cd545e9926de94117f2a46be5801c24271ba8))
* made LR inherit from BaseClassifier ([d06a7db](https://github.com/f-aguzzi/tesi/commit/d06a7db270a99517a6445c94bdfacc1901e90121))


### Bug Fixes

* lda and lr_tests missing arguments ([280159d](https://github.com/f-aguzzi/tesi/commit/280159d8208f46a2a843e9eeae60d82114e15261))


### Docs

* fix broken github pages build ([862ddf6](https://github.com/f-aguzzi/tesi/commit/862ddf6557973229ec9b85830b677822db0f9da7))
* fix wrong version number ([a0eb4e6](https://github.com/f-aguzzi/tesi/commit/a0eb4e6110dc25a5a8a4e6e72ff7ba02c05f6a14))
* new blog post ([afed9f7](https://github.com/f-aguzzi/tesi/commit/afed9f7620d06559892a517daef4f78192d3f3e2))
* new cookbook section ([fd9a243](https://github.com/f-aguzzi/tesi/commit/fd9a2435469bdcf0457909ec3424ce1af5b118a9))
* new version ([7c96050](https://github.com/f-aguzzi/tesi/commit/7c96050e20382fdd2312584dd0cf8ee091329181))
* update examples ([c919596](https://github.com/f-aguzzi/tesi/commit/c919596c94a7fd0c54548027d05c857c758054c9))
* updated docusaurus with versioning ([0b6d5c4](https://github.com/f-aguzzi/tesi/commit/0b6d5c4319f371a757ad0fc3a142e2eb1d959137)), closes [#33](https://github.com/f-aguzzi/tesi/issues/33)


### Refactor

* moved prediction into base class ([57a3497](https://github.com/f-aguzzi/tesi/commit/57a349743964db553aa6cea425631022c37920b3))
* **lldf:** switch arguments in constructor call ([fcf7471](https://github.com/f-aguzzi/tesi/commit/fcf7471ba519ceed7747f48895421e932506b835))


### CI

* **release:** 2.0.0-beta.1 [skip ci] ([6c4af27](https://github.com/f-aguzzi/tesi/commit/6c4af27e2d24a62ea91d4701bd1100ad2ea51801)), closes [#33](https://github.com/f-aguzzi/tesi/issues/33)
* **release:** 2.0.0-beta.2 [skip ci] ([c6892a9](https://github.com/f-aguzzi/tesi/commit/c6892a9d4f8e6e0cece469139c6c834e60d1f7bf))
* **release:** 2.0.0-beta.3 [skip ci] ([b9bd5e0](https://github.com/f-aguzzi/tesi/commit/b9bd5e0be28eeb3b9ea53a6ddb871a4532685184))
* **release:** 2.0.0-beta.4 [skip ci] ([330ad59](https://github.com/f-aguzzi/tesi/commit/330ad59b45e2ca435f0159c7a2ff656ca2e78570))

## [2.0.0-beta.4](https://github.com/f-aguzzi/tesi/compare/v2.0.0-beta.3...v2.0.0-beta.4) (2024-06-04)


### Bug Fixes

* lda and lr_tests missing arguments ([280159d](https://github.com/f-aguzzi/tesi/commit/280159d8208f46a2a843e9eeae60d82114e15261))


### Docs

* new blog post ([afed9f7](https://github.com/f-aguzzi/tesi/commit/afed9f7620d06559892a517daef4f78192d3f3e2))

## [2.0.0-beta.3](https://github.com/f-aguzzi/tesi/compare/v2.0.0-beta.2...v2.0.0-beta.3) (2024-06-04)


### Features

* **LDA:** autodetect components from PCADataModel ([a59cd54](https://github.com/f-aguzzi/tesi/commit/a59cd545e9926de94117f2a46be5801c24271ba8))


### Docs

* fix wrong version number ([a0eb4e6](https://github.com/f-aguzzi/tesi/commit/a0eb4e6110dc25a5a8a4e6e72ff7ba02c05f6a14))
* update examples ([c919596](https://github.com/f-aguzzi/tesi/commit/c919596c94a7fd0c54548027d05c857c758054c9))


### Refactor

* moved prediction into base class ([57a3497](https://github.com/f-aguzzi/tesi/commit/57a349743964db553aa6cea425631022c37920b3))
* **lldf:** switch arguments in constructor call ([fcf7471](https://github.com/f-aguzzi/tesi/commit/fcf7471ba519ceed7747f48895421e932506b835))

## [2.0.0-beta.2](https://github.com/f-aguzzi/tesi/compare/v2.0.0-beta.1...v2.0.0-beta.2) (2024-06-04)


### Features

* made LR inherit from BaseClassifier ([d06a7db](https://github.com/f-aguzzi/tesi/commit/d06a7db270a99517a6445c94bdfacc1901e90121))


### Docs

* new version ([7c96050](https://github.com/f-aguzzi/tesi/commit/7c96050e20382fdd2312584dd0cf8ee091329181))

## [2.0.0-beta.1](https://github.com/f-aguzzi/tesi/compare/v1.2.0...v2.0.0-beta.1) (2024-06-04)


### ⚠ BREAKING CHANGES

* added base class for classifiers, models, settings

### Features

* added base class for classifiers, models, settings ([4af5d47](https://github.com/f-aguzzi/tesi/commit/4af5d4778d28021dcd2e23f00fc5810ae178769d))


### Docs

* fix broken github pages build ([862ddf6](https://github.com/f-aguzzi/tesi/commit/862ddf6557973229ec9b85830b677822db0f9da7))
* new cookbook section ([fd9a243](https://github.com/f-aguzzi/tesi/commit/fd9a2435469bdcf0457909ec3424ce1af5b118a9))
* updated docusaurus with versioning ([0b6d5c4](https://github.com/f-aguzzi/tesi/commit/0b6d5c4319f371a757ad0fc3a142e2eb1d959137)), closes [#33](https://github.com/f-aguzzi/tesi/issues/33)

## [1.2.0](https://github.com/f-aguzzi/tesi/compare/v1.1.3...v1.2.0) (2024-06-03)


### Features

* graphing and multi-table in LLDF ([c450767](https://github.com/f-aguzzi/tesi/commit/c4507672fb502dfd5d9b0994ff461387ff5a3acc))


### Bug Fixes

* docs workflow, dependency clashes, demos ([a994940](https://github.com/f-aguzzi/tesi/commit/a994940a6bf115ea02054754fb3b237977a4e3aa)), closes [#29](https://github.com/f-aguzzi/tesi/issues/29) [#28](https://github.com/f-aguzzi/tesi/issues/28)
* docs workflow, dependency clashes, demos ([6f72ec4](https://github.com/f-aguzzi/tesi/commit/6f72ec4a0c51902e05e468b6d6f79042a3bc73e5)), closes [#29](https://github.com/f-aguzzi/tesi/issues/29) [#28](https://github.com/f-aguzzi/tesi/issues/28)
* gh pages workflow ([49c6bda](https://github.com/f-aguzzi/tesi/commit/49c6bdabf757073e87e0c7b0c98eb4d0ef843f78))


### Docs

* add documentation versioning [skip ci] ([ee0b7ab](https://github.com/f-aguzzi/tesi/commit/ee0b7ab915501d30d12ed6542535434265f0bd61))
* added version 1.2 ([3fcd0cc](https://github.com/f-aguzzi/tesi/commit/3fcd0cc7abdb5daa201c74ba959340711506e1f0))


### CI

* **release:** 1.1.1-beta.2 [skip ci] ([a0519e7](https://github.com/f-aguzzi/tesi/commit/a0519e71d2bc75830ce027bdb11589a0762905a8)), closes [#25](https://github.com/f-aguzzi/tesi/issues/25)
* **release:** 1.1.1-beta.3 [skip ci] ([4dc43c6](https://github.com/f-aguzzi/tesi/commit/4dc43c6f2e7ec6e34e6adfb5ad1b2aacaa3731e2)), closes [#29](https://github.com/f-aguzzi/tesi/issues/29) [#28](https://github.com/f-aguzzi/tesi/issues/28)
* **release:** 1.1.2-beta.1 [skip ci] ([a903084](https://github.com/f-aguzzi/tesi/commit/a9030846e88a15dfd9ec8a9418e59098ef4e439c)), closes [#29](https://github.com/f-aguzzi/tesi/issues/29) [#28](https://github.com/f-aguzzi/tesi/issues/28) [#25](https://github.com/f-aguzzi/tesi/issues/25) [#29](https://github.com/f-aguzzi/tesi/issues/29) [#28](https://github.com/f-aguzzi/tesi/issues/28)
* **release:** 1.1.2-beta.2 [skip ci] ([c23bcb0](https://github.com/f-aguzzi/tesi/commit/c23bcb0e833ed10ff7665f56edd82c0617152156)), closes [#29](https://github.com/f-aguzzi/tesi/issues/29) [#28](https://github.com/f-aguzzi/tesi/issues/28)
* **release:** 1.1.2-beta.3 [skip ci] ([0bcdf85](https://github.com/f-aguzzi/tesi/commit/0bcdf851d60b16c3e4ced0f562149490d6bcbcbe))
* **release:** 1.1.4-beta.1 [skip ci] ([d1e06cc](https://github.com/f-aguzzi/tesi/commit/d1e06cc4238c3e4f1b86ce4e8ab7e3eac6c5d1c6)), closes [#29](https://github.com/f-aguzzi/tesi/issues/29) [#28](https://github.com/f-aguzzi/tesi/issues/28) [#29](https://github.com/f-aguzzi/tesi/issues/29) [#28](https://github.com/f-aguzzi/tesi/issues/28) [#25](https://github.com/f-aguzzi/tesi/issues/25) [#29](https://github.com/f-aguzzi/tesi/issues/29) [#28](https://github.com/f-aguzzi/tesi/issues/28) [#29](https://github.com/f-aguzzi/tesi/issues/29) [#28](https://github.com/f-aguzzi/tesi/issues/28) [#25](https://github.com/f-aguzzi/tesi/issues/25) [#29](https://github.com/f-aguzzi/tesi/issues/29) [#28](https://github.com/f-aguzzi/tesi/issues/28) [#29](https://github.com/f-aguzzi/tesi/issues/29) [#28](https://github.com/f-aguzzi/tesi/issues/28)
* **release:** 1.2.0-beta.1 [skip ci] ([b08fa39](https://github.com/f-aguzzi/tesi/commit/b08fa3970d537a19072b70edb2275488d160d69f))

## [1.2.0-beta.1](https://github.com/f-aguzzi/tesi/compare/v1.1.4-beta.1...v1.2.0-beta.1) (2024-06-03)


### Features

* graphing and multi-table in LLDF ([c450767](https://github.com/f-aguzzi/tesi/commit/c4507672fb502dfd5d9b0994ff461387ff5a3acc))

## [1.1.4-beta.1](https://github.com/f-aguzzi/tesi/compare/v1.1.3...v1.1.4-beta.1) (2024-06-03)


### Bug Fixes

* docs workflow, dependency clashes, demos ([a994940](https://github.com/f-aguzzi/tesi/commit/a994940a6bf115ea02054754fb3b237977a4e3aa)), closes [#29](https://github.com/f-aguzzi/tesi/issues/29) [#28](https://github.com/f-aguzzi/tesi/issues/28)
* docs workflow, dependency clashes, demos ([6f72ec4](https://github.com/f-aguzzi/tesi/commit/6f72ec4a0c51902e05e468b6d6f79042a3bc73e5)), closes [#29](https://github.com/f-aguzzi/tesi/issues/29) [#28](https://github.com/f-aguzzi/tesi/issues/28)
* gh pages workflow ([49c6bda](https://github.com/f-aguzzi/tesi/commit/49c6bdabf757073e87e0c7b0c98eb4d0ef843f78))


### Docs

* add documentation versioning [skip ci] ([ee0b7ab](https://github.com/f-aguzzi/tesi/commit/ee0b7ab915501d30d12ed6542535434265f0bd61))
* added version 1.2 ([3fcd0cc](https://github.com/f-aguzzi/tesi/commit/3fcd0cc7abdb5daa201c74ba959340711506e1f0))


### CI

* **release:** 1.1.1-beta.2 [skip ci] ([a0519e7](https://github.com/f-aguzzi/tesi/commit/a0519e71d2bc75830ce027bdb11589a0762905a8)), closes [#25](https://github.com/f-aguzzi/tesi/issues/25)
* **release:** 1.1.1-beta.3 [skip ci] ([4dc43c6](https://github.com/f-aguzzi/tesi/commit/4dc43c6f2e7ec6e34e6adfb5ad1b2aacaa3731e2)), closes [#29](https://github.com/f-aguzzi/tesi/issues/29) [#28](https://github.com/f-aguzzi/tesi/issues/28)
* **release:** 1.1.2-beta.1 [skip ci] ([a903084](https://github.com/f-aguzzi/tesi/commit/a9030846e88a15dfd9ec8a9418e59098ef4e439c)), closes [#29](https://github.com/f-aguzzi/tesi/issues/29) [#28](https://github.com/f-aguzzi/tesi/issues/28) [#25](https://github.com/f-aguzzi/tesi/issues/25) [#29](https://github.com/f-aguzzi/tesi/issues/29) [#28](https://github.com/f-aguzzi/tesi/issues/28)
* **release:** 1.1.2-beta.2 [skip ci] ([c23bcb0](https://github.com/f-aguzzi/tesi/commit/c23bcb0e833ed10ff7665f56edd82c0617152156)), closes [#29](https://github.com/f-aguzzi/tesi/issues/29) [#28](https://github.com/f-aguzzi/tesi/issues/28)
* **release:** 1.1.2-beta.3 [skip ci] ([0bcdf85](https://github.com/f-aguzzi/tesi/commit/0bcdf851d60b16c3e4ced0f562149490d6bcbcbe))

## [1.1.3](https://github.com/f-aguzzi/tesi/compare/v1.1.2...v1.1.3) (2024-05-29)


### Bug Fixes

* numpy dependency clash ([cab6371](https://github.com/f-aguzzi/tesi/commit/cab6371b993b4019cb2d223d1e20759ab642c30a))

## [1.1.2](https://github.com/f-aguzzi/tesi/compare/v1.1.1...v1.1.2) (2024-05-29)


### Bug Fixes

* updated paths and triggers in workflows ([6a5fd55](https://github.com/f-aguzzi/tesi/commit/6a5fd55592446e7fcbf99fc390562c0574771cb2))

## [1.1.2-beta.3](https://github.com/f-aguzzi/tesi/compare/v1.1.2-beta.2...v1.1.2-beta.3) (2024-05-29)


### Bug Fixes

* gh pages workflow ([49c6bda](https://github.com/f-aguzzi/tesi/commit/49c6bdabf757073e87e0c7b0c98eb4d0ef843f78))

## [1.1.2-beta.2](https://github.com/f-aguzzi/tesi/compare/v1.1.2-beta.1...v1.1.2-beta.2) (2024-05-29)


### Bug Fixes

* docs workflow, dependency clashes, demos ([a994940](https://github.com/f-aguzzi/tesi/commit/a994940a6bf115ea02054754fb3b237977a4e3aa)), closes [#29](https://github.com/f-aguzzi/tesi/issues/29) [#28](https://github.com/f-aguzzi/tesi/issues/28)

## [1.1.2-beta.1](https://github.com/f-aguzzi/tesi/compare/v1.1.1...v1.1.2-beta.1) (2024-05-29)


### Bug Fixes

* docs workflow, dependency clashes, demos ([6f72ec4](https://github.com/f-aguzzi/tesi/commit/6f72ec4a0c51902e05e468b6d6f79042a3bc73e5)), closes [#29](https://github.com/f-aguzzi/tesi/issues/29) [#28](https://github.com/f-aguzzi/tesi/issues/28)


### CI

* **release:** 1.1.1-beta.2 [skip ci] ([a0519e7](https://github.com/f-aguzzi/tesi/commit/a0519e71d2bc75830ce027bdb11589a0762905a8)), closes [#25](https://github.com/f-aguzzi/tesi/issues/25)
* **release:** 1.1.1-beta.3 [skip ci] ([4dc43c6](https://github.com/f-aguzzi/tesi/commit/4dc43c6f2e7ec6e34e6adfb5ad1b2aacaa3731e2)), closes [#29](https://github.com/f-aguzzi/tesi/issues/29) [#28](https://github.com/f-aguzzi/tesi/issues/28)

## [1.1.1-beta.3](https://github.com/f-aguzzi/tesi/compare/v1.1.1-beta.2...v1.1.1-beta.3) (2024-05-29)


### Bug Fixes


* docs workflow, dependency clashes, demos ([6f72ec4](https://github.com/f-aguzzi/tesi/commit/6f72ec4a0c51902e05e468b6d6f79042a3bc73e5)), closes [#29](https://github.com/f-aguzzi/tesi/issues/29) [#28](https://github.com/f-aguzzi/tesi/issues/28)

## [1.1.1-beta.2](https://github.com/f-aguzzi/tesi/compare/v1.1.1-beta.1...v1.1.1-beta.2) (2024-05-24)


### Bug Fixes

* wrong training procedure in SVM ([#25](https://github.com/f-aguzzi/tesi/issues/25)) ([7f25487](https://github.com/f-aguzzi/tesi/commit/7f254876fcdbd2ba5c46278d31eb851a50659e8f))
* wrong training procedure in SVM ([74d1741](https://github.com/f-aguzzi/tesi/commit/74d1741743f53eea6cc2d9002005c6426bf4f0d0))
* wrong training procedure in SVM ([#25](https://github.com/f-aguzzi/tesi/issues/25)) ([7f25487](https://github.com/f-aguzzi/tesi/commit/7f254876fcdbd2ba5c46278d31eb851a50659e8f))


### CI

* **release:** 1.1.0-beta.3 [skip ci] ([96988ac](https://github.com/f-aguzzi/tesi/commit/96988acbfd0f015c03385f74f14ea26e98a9b4b2))
* **release:** 1.1.1-beta.1 [skip ci] ([a6e41a8](https://github.com/f-aguzzi/tesi/commit/a6e41a88456fc8224c0864de40eb2233c0c30329))


## [1.1.1-beta.1](https://github.com/f-aguzzi/tesi/compare/v1.1.0...v1.1.1-beta.1) (2024-05-23)


### Bug Fixes

* wrong training procedure in SVM ([74d1741](https://github.com/f-aguzzi/tesi/commit/74d1741743f53eea6cc2d9002005c6426bf4f0d0))


### CI

* **release:** 1.1.0-beta.3 [skip ci] ([96988ac](https://github.com/f-aguzzi/tesi/commit/96988acbfd0f015c03385f74f14ea26e98a9b4b2))

## [1.1.0-beta.3](https://github.com/f-aguzzi/tesi/compare/v1.1.0-beta.2...v1.1.0-beta.3) (2024-05-23)


### Features

* beartype integration ([2f823ce](https://github.com/f-aguzzi/tesi/commit/2f823cebee0cb8006523d9e0d6aaa673484bd928)), closes [#7](https://github.com/f-aguzzi/tesi/issues/7)


### Bug Fixes


* wrong training procedure in SVM ([74d1741](https://github.com/f-aguzzi/tesi/commit/74d1741743f53eea6cc2d9002005c6426bf4f0d0))

* add missing checks to LLDFSettings ([3d57752](https://github.com/f-aguzzi/tesi/commit/3d577527eefd0b183a66c378d53cb1f1ee506343)), closes [#20](https://github.com/f-aguzzi/tesi/issues/20)


### chore

* **thesis:** set up build system (merge from [#22](https://github.com/f-aguzzi/tesi/issues/22)) ([0b13ed3](https://github.com/f-aguzzi/tesi/commit/0b13ed346448f0eeefecbc6fd051eb7c98919650))


### Refactor

* extract split tests and graphs (merge [#23](https://github.com/f-aguzzi/tesi/issues/23)) ([6865c88](https://github.com/f-aguzzi/tesi/commit/6865c88d70b650de5e8440807b0194022a15dc0e))


### CI

* **release:** 1.1.0-beta.1 [skip ci] ([2deffcc](https://github.com/f-aguzzi/tesi/commit/2deffcc4c8a29d09a4a644558e491d770f71f6dc)), closes [#7](https://github.com/f-aguzzi/tesi/issues/7)
* **release:** 1.1.0-beta.2 [skip ci] ([25704dc](https://github.com/f-aguzzi/tesi/commit/25704dc4eb0cbc249bbf85611c5dfe257ebccc30)), closes [#20](https://github.com/f-aguzzi/tesi/issues/20) [#22](https://github.com/f-aguzzi/tesi/issues/22) [#23](https://github.com/f-aguzzi/tesi/issues/23)


## [1.1.0-beta.2](https://github.com/f-aguzzi/tesi/compare/v1.1.0-beta.1...v1.1.0-beta.2) (2024-05-20)


### Bug Fixes

* add missing checks to LLDFSettings ([3d57752](https://github.com/f-aguzzi/tesi/commit/3d577527eefd0b183a66c378d53cb1f1ee506343)), closes [#20](https://github.com/f-aguzzi/tesi/issues/20)


### chore

* **thesis:** set up build system (merge from [#22](https://github.com/f-aguzzi/tesi/issues/22)) ([0b13ed3](https://github.com/f-aguzzi/tesi/commit/0b13ed346448f0eeefecbc6fd051eb7c98919650))


### Refactor

* extract split tests and graphs (merge [#23](https://github.com/f-aguzzi/tesi/issues/23)) ([6865c88](https://github.com/f-aguzzi/tesi/commit/6865c88d70b650de5e8440807b0194022a15dc0e))

## [1.1.0-beta.1](https://github.com/f-aguzzi/tesi/compare/v1.0.0...v1.1.0-beta.1) (2024-05-18)


### Features

* beartype integration ([2f823ce](https://github.com/f-aguzzi/tesi/commit/2f823cebee0cb8006523d9e0d6aaa673484bd928)), closes [#7](https://github.com/f-aguzzi/tesi/issues/7)

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
