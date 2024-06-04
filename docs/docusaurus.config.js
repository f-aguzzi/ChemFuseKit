// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';
const simplePlantUML = require("@akebifiky/remark-simple-plantuml");

/** @type {import('@docusaurus/types').Config} */
const config = {
  markdown: {
    mermaid: true,
  },
  themes: ['@docusaurus/theme-mermaid'],

  title: 'ChemFuseKit: Colab Data Fusion and Analysis',
  tagline: 'Chemometrics on the go',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://f-aguzzi.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/tesi/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'f-aguzzi', // Usually your GitHub org/user name.
  projectName: 'tesi', // Usually your repo name.

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/f-aguzzi/tesi',
          remarkPlugins: [simplePlantUML],
        },
        pages: {
          path: 'src/pages',
          routeBasePath: '',
          remarkPlugins: [simplePlantUML],
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  plugins: [
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'cookbook',
        path: 'cookbook',
        routeBasePath: 'cookbook',
        sidebarPath: './sidebarsCookbook.js',
        // ... other options
      },
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: 'img/docusaurus-social-card.jpg',
      navbar: {
        title: 'Homepage',
        logo: {
          alt: 'My Site Logo',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Docs',
          },
          {
            to: '/project/',
            label: 'Project',
            position: 'left',
          },
          {
            type: 'docSidebar',
            docsPluginId: 'cookbook',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Cookbook',
          },
          {
            type: 'docsVersionDropdown',
            label: 'Docs version',
            position: 'right'
          },
          {
            to: 'blog',
            label: 'Blog',
            position: 'right'
          },
          {
            href: 'https://github.com/f-aguzzi/tesi',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Docs',
            items: [
              {
                label: 'Tutorial',
                to: '/docs/tutorial',
              },
            ],
          },
          /*
          {
            title: 'Community',
            items: [
              {
                label: 'Stack Overflow',
                href: 'https://stackoverflow.com/questions/tagged/docusaurus',
              },
              {
                label: 'Discord',
                href: 'https://discordapp.com/invite/docusaurus',
              },
              {
                label: 'Twitter',
                href: 'https://twitter.com/docusaurus',
              },
            ],
          },
          */
          {
            title: 'More',
            items: [ 
              {
                label: 'GitHub',
                href: 'https://github.com/f-aguzzi/tesi',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Federico Aguzzi, Università degli Studi di Bergamo. Built with Docusaurus.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
};

export default config;
