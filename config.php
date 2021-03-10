<?php
define('WP_AUTO_UPDATE_CORE', 'minor');// This setting is required to make sure that WordPress updates can be properly managed in WordPress Toolkit. Remove this line if this WordPress website is not managed by WordPress Toolkit anymore.
/**
 * The base configurations of the WordPress.
 *
 * This file has the following configurations: MySQL settings, Table Prefix,
 * Secret Keys, WordPress Language, and ABSPATH. You can find more information
 * by visiting {@link http://codex.wordpress.org/Editing_wp-config.php Editing
 * wp-config.php} Codex page. You can get the MySQL settings from your web host.
 *
 * This file is used by the wp-config.php creation script during the
 * installation. You don't have to use the web site, you can just copy this file
 * to "wp-config.php" and fill in the values.
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', 'chouse_kalypsowpdbgr');

/** MySQL database username */
define('DB_USER', 'kalypsus_dbuser');

/** MySQL database password */
define('DB_PASSWORD', 'M5~id9hxbNP@');

/** MySQL hostname */
define('DB_HOST', 'localhost');

/** Database Charset to use in creating database tables. */
define('DB_CHARSET', 'utf8');

/** The Database Collate type. Don't change this if in doubt. */
define('DB_COLLATE', '');

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define('AUTH_KEY',         '~+rlv@V0;$Gd-|5iQ4lQ(?+7AgIw+.*o6a8]?15l7XZpb7<GdIyYTi<!sm4r.<UM');
define('SECURE_AUTH_KEY',  'UJ$ne1p<)?N++c3r:4N#_z $IGn&/A%DcsIbQ*ZznGmv-EKDk/NUU Q`!Z^,WlW%');
define('LOGGED_IN_KEY',    'j.(Ur j`+Q+B~{sWNgRT(VdaKoXw8Qi^<nRiDoTh*J?07gU[S05#%y8M+}>:L^C ');
define('NONCE_KEY',        'o-5*v<|SakNX_}1+[}[=fREycL6*QzE*&a+OOY0U<kj@ZCj`obn&yz*xbgc{7|}-');
define('AUTH_SALT',        'm0BVxusU+]9ioO Ia4n8?%70-SHx90;UK_y=~c|L<{JVit&YgIm+/b}s<;jgqe?X');
define('SECURE_AUTH_SALT', '01O1Tpv]LpP-xqqB{0+gym|c(^tmmA=U#@~]xU< -|{5mS3EALG,aXbcX@_c`N`v');
define('LOGGED_IN_SALT',   '-dqNd&NqtvhJgiA`h-D/^fPo@B%arMlKILgx4M1b#{w+$F|/B*^z*/dW19:rh([I');
define('NONCE_SALT',       'B:NlEM[v5|tj,-Xu1fk|FsBYp;0 $=N+k!2[Gma4>HF?E`3P j^VkB!{OL|bix+*');

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each a unique
 * prefix. Only numbers, letters, and underscores please!
 */
$table_prefix  = 'wp_';

/**
 * WordPress Localized Language, defaults to English.
 *
 * Change this to localize WordPress. A corresponding MO file for the chosen
 * language must be installed to wp-content/languages. For example, install
 * de_DE.mo to wp-content/languages and set WPLANG to 'de_DE' to enable German
 * language support.
 */
define('WPLANG', '');

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 */
define('WP_DEBUG', false);

/* That's all, stop editing! Happy blogging. */

/** Absolute path to the WordPress directory. */
if ( !defined('ABSPATH') )
	define('ABSPATH', dirname(__FILE__) . '/');

/** Sets up WordPress vars and included files. */
require_once(ABSPATH . 'wp-settings.php');
