import lume from "lume/mod.ts";
import base_path from "lume/plugins/base_path.ts";
import date from "lume/plugins/date.ts";
import metas from "lume/plugins/metas.ts";
import postcss from "lume/plugins/postcss.ts";

// Importing the OI Lume charts and utilities
import oiViz from "https://deno.land/x/oi_lume_viz@v0.15.11/mod.ts";
import autoDependency from "https://deno.land/x/oi_lume_utils@v0.4.0/processors/auto-dependency.ts";
import csvLoader from "https://deno.land/x/oi_lume_utils@v0.4.0/loaders/csv-loader.ts";
import jsonLoader from "lume/core/loaders/json.ts";

const site = lume({
  src: './src',
  location: new URL("https://taz-chiles.github.io/mental-health-data-explorer/"),
});

site.loadData([".csv", ".tsv", ".dat"], csvLoader({ basic: true }));
site.loadData([".geojson"], jsonLoader);
site.loadData([".hexjson"], jsonLoader);

// Import lume viz
import oiVizConfig from "./oi-viz-config.ts";
site.use(oiViz(oiVizConfig));

site.use(oiViz({
	assetPath: '/assets/oi',
	componentNamespace: 'oi.viz'
}));

site.use(base_path());
site.use(metas({
  defaultPageData: {
    title: 'Mental Health Explorer', // Use the `date` value as fallback.
  },
}));
site.use(date());
site.use(postcss({}));

site.copy('CNAME');
site.copy('assets/images');
site.copy('assets/css/fonts');
site.copy('.nojekyll');

export default site;
