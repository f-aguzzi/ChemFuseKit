import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'Easy to Use',
    Svg: require('@site/static/img/happy-woman.svg').default,
    description: (
      <>
        This library was designed from the ground up to be easily distributed and
        used to get your chemical analysis up and running quickly.
      </>
    ),
  },
  {
    title: 'Focus on What Matters',
    Svg: require('@site/static/img/magnifying-glass.svg').default,
    description: (
      <>
        This library lets you focus on your data, and we&apos;ll do the chores. Go
        ahead and forget all the hard parts about data handling.
      </>
    ),
  },
  {
    title: 'Powered by Colab',
    Svg: require('@site/static/img/colab-logo.svg').default,
    description: (
      <>
        Get your data processed blazingly fast thanks to Google's Colab
        platform.
      </>
    ),
  },
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
