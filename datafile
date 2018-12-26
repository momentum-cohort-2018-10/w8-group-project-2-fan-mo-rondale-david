--
-- PostgreSQL database dump
--

-- Dumped from database version 10.5
-- Dumped by pg_dump version 10.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: DATABASE questionbox; Type: COMMENT; Schema: -; Owner: fan
--

COMMENT ON DATABASE questionbox IS 'questionbox';


--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: questionbox
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO questionbox;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: questionbox
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO questionbox;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: questionbox
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: questionbox
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO questionbox;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: questionbox
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO questionbox;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: questionbox
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: questionbox
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO questionbox;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: questionbox
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO questionbox;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: questionbox
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: authtoken_token; Type: TABLE; Schema: public; Owner: questionbox
--

CREATE TABLE public.authtoken_token (
    key character varying(40) NOT NULL,
    created timestamp with time zone NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.authtoken_token OWNER TO questionbox;

--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: questionbox
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO questionbox;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: questionbox
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO questionbox;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: questionbox
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: questionbox
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO questionbox;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: questionbox
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO questionbox;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: questionbox
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: questionbox
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO questionbox;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: questionbox
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO questionbox;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: questionbox
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: questionbox
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO questionbox;

--
-- Name: questions_answer; Type: TABLE; Schema: public; Owner: questionbox
--

CREATE TABLE public.questions_answer (
    id integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    text text NOT NULL,
    author_id integer NOT NULL,
    question_id integer
);


ALTER TABLE public.questions_answer OWNER TO questionbox;

--
-- Name: questions_answer_id_seq; Type: SEQUENCE; Schema: public; Owner: questionbox
--

CREATE SEQUENCE public.questions_answer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.questions_answer_id_seq OWNER TO questionbox;

--
-- Name: questions_answer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: questionbox
--

ALTER SEQUENCE public.questions_answer_id_seq OWNED BY public.questions_answer.id;


--
-- Name: questions_profile; Type: TABLE; Schema: public; Owner: questionbox
--

CREATE TABLE public.questions_profile (
    id integer NOT NULL,
    image character varying(100) NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.questions_profile OWNER TO questionbox;

--
-- Name: questions_profile_id_seq; Type: SEQUENCE; Schema: public; Owner: questionbox
--

CREATE SEQUENCE public.questions_profile_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.questions_profile_id_seq OWNER TO questionbox;

--
-- Name: questions_profile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: questionbox
--

ALTER SEQUENCE public.questions_profile_id_seq OWNED BY public.questions_profile.id;


--
-- Name: questions_question; Type: TABLE; Schema: public; Owner: questionbox
--

CREATE TABLE public.questions_question (
    id integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    title character varying(255),
    text text NOT NULL,
    author_id integer NOT NULL
);


ALTER TABLE public.questions_question OWNER TO questionbox;

--
-- Name: questions_question_id_seq; Type: SEQUENCE; Schema: public; Owner: questionbox
--

CREATE SEQUENCE public.questions_question_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.questions_question_id_seq OWNER TO questionbox;

--
-- Name: questions_question_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: questionbox
--

ALTER SEQUENCE public.questions_question_id_seq OWNED BY public.questions_question.id;


--
-- Name: questions_starreditem; Type: TABLE; Schema: public; Owner: questionbox
--

CREATE TABLE public.questions_starreditem (
    id integer NOT NULL,
    object_id integer NOT NULL,
    content_type_id integer NOT NULL,
    user_id integer NOT NULL,
    CONSTRAINT questions_starreditem_object_id_check CHECK ((object_id >= 0))
);


ALTER TABLE public.questions_starreditem OWNER TO questionbox;

--
-- Name: questions_starreditem_id_seq; Type: SEQUENCE; Schema: public; Owner: questionbox
--

CREATE SEQUENCE public.questions_starreditem_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.questions_starreditem_id_seq OWNER TO questionbox;

--
-- Name: questions_starreditem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: questionbox
--

ALTER SEQUENCE public.questions_starreditem_id_seq OWNED BY public.questions_starreditem.id;


--
-- Name: questions_user; Type: TABLE; Schema: public; Owner: questionbox
--

CREATE TABLE public.questions_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.questions_user OWNER TO questionbox;

--
-- Name: questions_user_groups; Type: TABLE; Schema: public; Owner: questionbox
--

CREATE TABLE public.questions_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.questions_user_groups OWNER TO questionbox;

--
-- Name: questions_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: questionbox
--

CREATE SEQUENCE public.questions_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.questions_user_groups_id_seq OWNER TO questionbox;

--
-- Name: questions_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: questionbox
--

ALTER SEQUENCE public.questions_user_groups_id_seq OWNED BY public.questions_user_groups.id;


--
-- Name: questions_user_id_seq; Type: SEQUENCE; Schema: public; Owner: questionbox
--

CREATE SEQUENCE public.questions_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.questions_user_id_seq OWNER TO questionbox;

--
-- Name: questions_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: questionbox
--

ALTER SEQUENCE public.questions_user_id_seq OWNED BY public.questions_user.id;


--
-- Name: questions_user_user_permissions; Type: TABLE; Schema: public; Owner: questionbox
--

CREATE TABLE public.questions_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.questions_user_user_permissions OWNER TO questionbox;

--
-- Name: questions_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: questionbox
--

CREATE SEQUENCE public.questions_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.questions_user_user_permissions_id_seq OWNER TO questionbox;

--
-- Name: questions_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: questionbox
--

ALTER SEQUENCE public.questions_user_user_permissions_id_seq OWNED BY public.questions_user_user_permissions.id;


--
-- Name: registration_registrationprofile; Type: TABLE; Schema: public; Owner: questionbox
--

CREATE TABLE public.registration_registrationprofile (
    id integer NOT NULL,
    activation_key character varying(40) NOT NULL,
    user_id integer NOT NULL,
    activated boolean NOT NULL
);


ALTER TABLE public.registration_registrationprofile OWNER TO questionbox;

--
-- Name: registration_registrationprofile_id_seq; Type: SEQUENCE; Schema: public; Owner: questionbox
--

CREATE SEQUENCE public.registration_registrationprofile_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.registration_registrationprofile_id_seq OWNER TO questionbox;

--
-- Name: registration_registrationprofile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: questionbox
--

ALTER SEQUENCE public.registration_registrationprofile_id_seq OWNED BY public.registration_registrationprofile.id;


--
-- Name: registration_supervisedregistrationprofile; Type: TABLE; Schema: public; Owner: questionbox
--

CREATE TABLE public.registration_supervisedregistrationprofile (
    registrationprofile_ptr_id integer NOT NULL
);


ALTER TABLE public.registration_supervisedregistrationprofile OWNER TO questionbox;

--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: questions_answer id; Type: DEFAULT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.questions_answer ALTER COLUMN id SET DEFAULT nextval('public.questions_answer_id_seq'::regclass);


--
-- Name: questions_profile id; Type: DEFAULT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.questions_profile ALTER COLUMN id SET DEFAULT nextval('public.questions_profile_id_seq'::regclass);


--
-- Name: questions_question id; Type: DEFAULT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.questions_question ALTER COLUMN id SET DEFAULT nextval('public.questions_question_id_seq'::regclass);


--
-- Name: questions_starreditem id; Type: DEFAULT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.questions_starreditem ALTER COLUMN id SET DEFAULT nextval('public.questions_starreditem_id_seq'::regclass);


--
-- Name: questions_user id; Type: DEFAULT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.questions_user ALTER COLUMN id SET DEFAULT nextval('public.questions_user_id_seq'::regclass);


--
-- Name: questions_user_groups id; Type: DEFAULT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.questions_user_groups ALTER COLUMN id SET DEFAULT nextval('public.questions_user_groups_id_seq'::regclass);


--
-- Name: questions_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.questions_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.questions_user_user_permissions_id_seq'::regclass);


--
-- Name: registration_registrationprofile id; Type: DEFAULT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.registration_registrationprofile ALTER COLUMN id SET DEFAULT nextval('public.registration_registrationprofile_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: questionbox
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: questionbox
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: questionbox
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add content type	4	add_contenttype
14	Can change content type	4	change_contenttype
15	Can delete content type	4	delete_contenttype
16	Can view content type	4	view_contenttype
17	Can add session	5	add_session
18	Can change session	5	change_session
19	Can delete session	5	delete_session
20	Can view session	5	view_session
21	Can add user	6	add_user
22	Can change user	6	change_user
23	Can delete user	6	delete_user
24	Can view user	6	view_user
25	Can add answer	7	add_answer
26	Can change answer	7	change_answer
27	Can delete answer	7	delete_answer
28	Can view answer	7	view_answer
29	Can add question	8	add_question
30	Can change question	8	change_question
31	Can delete question	8	delete_question
32	Can view question	8	view_question
33	Can add starred item	9	add_starreditem
34	Can change starred item	9	change_starreditem
35	Can delete starred item	9	delete_starreditem
36	Can view starred item	9	view_starreditem
37	Can add registration profile	10	add_registrationprofile
38	Can change registration profile	10	change_registrationprofile
39	Can delete registration profile	10	delete_registrationprofile
40	Can view registration profile	10	view_registrationprofile
41	Can add supervised registration profile	11	add_supervisedregistrationprofile
42	Can change supervised registration profile	11	change_supervisedregistrationprofile
43	Can delete supervised registration profile	11	delete_supervisedregistrationprofile
44	Can view supervised registration profile	11	view_supervisedregistrationprofile
45	Can add profile	12	add_profile
46	Can change profile	12	change_profile
47	Can delete profile	12	delete_profile
48	Can view profile	12	view_profile
49	Can add Token	13	add_token
50	Can change Token	13	change_token
51	Can delete Token	13	delete_token
52	Can view Token	13	view_token
\.


--
-- Data for Name: authtoken_token; Type: TABLE DATA; Schema: public; Owner: questionbox
--

COPY public.authtoken_token (key, created, user_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: questionbox
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
10	2018-12-20 09:10:12.467257-05	30	StarredItem object (30)	3		9	23
11	2018-12-20 09:10:12.509974-05	29	StarredItem object (29)	3		9	23
12	2018-12-20 09:10:12.516131-05	28	StarredItem object (28)	3		9	23
13	2018-12-20 09:10:12.517499-05	27	StarredItem object (27)	3		9	23
14	2018-12-20 09:10:12.520645-05	26	StarredItem object (26)	3		9	23
15	2018-12-20 09:10:12.522793-05	25	StarredItem object (25)	3		9	23
16	2018-12-20 09:10:12.524207-05	24	StarredItem object (24)	3		9	23
17	2018-12-20 09:10:12.525508-05	23	StarredItem object (23)	3		9	23
18	2018-12-20 09:10:12.529284-05	22	StarredItem object (22)	3		9	23
19	2018-12-20 09:10:12.530522-05	21	StarredItem object (21)	3		9	23
20	2018-12-20 09:10:12.531682-05	20	StarredItem object (20)	3		9	23
21	2018-12-20 09:10:12.533034-05	19	StarredItem object (19)	3		9	23
22	2018-12-20 09:10:12.534332-05	18	StarredItem object (18)	3		9	23
23	2018-12-20 09:10:12.536317-05	17	StarredItem object (17)	3		9	23
24	2018-12-20 09:10:12.53841-05	16	StarredItem object (16)	3		9	23
25	2018-12-20 09:10:12.539958-05	15	StarredItem object (15)	3		9	23
26	2018-12-20 09:10:12.541125-05	14	StarredItem object (14)	3		9	23
27	2018-12-20 09:10:12.542377-05	13	StarredItem object (13)	3		9	23
28	2018-12-20 09:10:12.546236-05	12	StarredItem object (12)	3		9	23
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: questionbox
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	contenttypes	contenttype
5	sessions	session
6	questions	user
7	questions	answer
8	questions	question
9	questions	starreditem
10	registration	registrationprofile
11	registration	supervisedregistrationprofile
12	questions	profile
13	authtoken	token
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: questionbox
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2018-12-17 13:41:55.783107-05
2	contenttypes	0002_remove_content_type_name	2018-12-17 13:41:55.836496-05
3	auth	0001_initial	2018-12-17 13:41:55.874236-05
4	auth	0002_alter_permission_name_max_length	2018-12-17 13:41:55.881124-05
5	auth	0003_alter_user_email_max_length	2018-12-17 13:41:55.887992-05
6	auth	0004_alter_user_username_opts	2018-12-17 13:41:55.896515-05
7	auth	0005_alter_user_last_login_null	2018-12-17 13:41:55.903241-05
8	auth	0006_require_contenttypes_0002	2018-12-17 13:41:55.905624-05
9	auth	0007_alter_validators_add_error_messages	2018-12-17 13:41:55.920765-05
10	auth	0008_alter_user_username_max_length	2018-12-17 13:41:55.940439-05
11	auth	0009_alter_user_last_name_max_length	2018-12-17 13:41:55.946621-05
12	questions	0001_initial	2018-12-17 13:41:56.076978-05
13	admin	0001_initial	2018-12-17 13:41:56.10159-05
14	admin	0002_logentry_remove_auto_add	2018-12-17 13:41:56.114747-05
15	admin	0003_logentry_add_action_flag_choices	2018-12-17 13:41:56.125529-05
16	sessions	0001_initial	2018-12-17 13:41:56.13814-05
17	registration	0001_initial	2018-12-17 17:35:52.011403-05
18	registration	0002_registrationprofile_activated	2018-12-17 17:35:52.032993-05
19	registration	0003_migrate_activatedstatus	2018-12-17 17:35:52.047569-05
20	registration	0004_supervisedregistrationprofile	2018-12-17 17:35:52.0658-05
21	questions	0002_auto_20181218_1439	2018-12-18 14:39:46.099533-05
22	questions	0003_auto_20181220_0909	2018-12-20 09:10:18.357901-05
23	questions	0003_profile	2018-12-20 12:13:35.188996-05
24	questions	0004_merge_20181221_0947	2018-12-21 09:47:12.474444-05
25	authtoken	0001_initial	2018-12-21 10:22:39.410461-05
26	authtoken	0002_auto_20160226_1747	2018-12-21 10:22:39.474832-05
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: questionbox
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
yokuenykhkhruvhdgo8p246m5tuy2qzf	YmIxZDU0ZDhiNzQ0ZWFhZjljNTExODViYTY5MTA5NjVjZTI1NDczZTp7Il9hdXRoX3VzZXJfaWQiOiIyMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZDQ3MDg3ZmMwZGY1NTQ1OTJkNDQxMDNkNGQzNmVkYjBmMWNlZGM1NSJ9	2019-01-04 14:00:33.497744-05
\.


--
-- Data for Name: questions_answer; Type: TABLE DATA; Schema: public; Owner: questionbox
--

COPY public.questions_answer (id, created_at, text, author_id, question_id) FROM stdin;
1354	2018-12-21 14:38:50.290746-05	Firm thousand summer visit eat tend. Choose out skin per. Call standard democratic daughter.\nMother such law according direction across despite mean. Check sport each spend. Such similar leave first capital bill.	165	540
1355	2018-12-21 14:38:50.30058-05	Common seem science media play occur. Involve information such center different during ability. Bank black professional peace.\nThough protect politics rule security. Almost amount court without budget.	168	526
1356	2018-12-21 14:38:50.30626-05	Science what sea natural. That once deep front.\nPer room cup none morning best town. Support entire government outside grow defense.\nIf recognize impact soldier large second. Structure cup manage action.	175	536
1357	2018-12-21 14:38:50.314505-05	Thus size anything service. Sort never management service democratic. List prove help land carry top court.\nEarly order building agree serious. Industry sell ago.	159	523
1358	2018-12-21 14:38:50.320508-05	Anyone remember hit rock draw few full. Develop news major north always its.\nTop quality institution quickly modern assume suffer energy. Compare less whatever size. Operation fast within life.\nStay case song. Center still man try task discover.	23	544
1359	2018-12-21 14:38:50.326304-05	Between one girl answer himself. Yourself current receive state let then.\nCampaign positive society natural quality music experience. Four build either city economic style region.\nStore about human see. Explain begin figure front with.	167	522
1360	2018-12-21 14:38:50.334153-05	Beautiful herself drive decade very message must. Specific could heavy body authority authority article. Meeting figure important national business.\nBoth interesting imagine usually night open nothing. Sister these interview appear.	160	550
1361	2018-12-21 14:38:50.339529-05	Site notice face. Idea rich season section develop end.\nDebate reason force eye main example dark. Table behind in fast product check support. Maintain gas response simply talk course.	23	523
1362	2018-12-21 14:38:50.347394-05	Argue coach section right loss professional. Clear beautiful huge decade hit enter. Six agency purpose cut among member again.\nState affect reach card.	168	541
1363	2018-12-21 14:38:50.352862-05	Type public song. Fish marriage break process woman south million strong. Make get consumer single son kid card.\nPerhaps loss fast dark color kid. Choice spring health either firm.	166	520
1364	2018-12-21 14:38:50.358566-05	North step race catch try rather current. Heavy apply after.\nWhether resource expect age play.\nFull firm indicate according. Through have enough media. Reason similar performance people.	167	533
1365	2018-12-21 14:38:50.366697-05	Leave bit financial still pattern education notice. Floor market lose kid. Strong born kitchen world.\nGround author why assume answer. Return between knowledge stage budget. Back system notice conference build production.	162	510
1366	2018-12-21 14:38:50.372522-05	Majority safe ability west arm whole.\nThat force hour tough then. Why bad fly morning million attack develop.\nEntire yourself bank whatever keep. Friend summer majority family. Establish maybe issue end politics. Seat hot your certainly floor.	171	536
1367	2018-12-21 14:38:50.379885-05	Beat food one wife. West billion leader represent guy deep. Trip public increase I consumer treatment few about.\nFine forward long such stuff hit approach. Sort season couple officer go sure long. Would ability cultural east play democratic.	162	533
1368	2018-12-21 14:38:50.387537-05	Example region policy great. Challenge out draw the against road face everybody. Before ten face current car pressure.\nBorn threat record suddenly.	168	536
1369	2018-12-21 14:38:50.396466-05	Professional officer parent relationship just long data. Kid grow across chance operation speech trade.\nOffer have consumer onto benefit cost. Sometimes meeting group source design face sometimes among.	159	520
1370	2018-12-21 14:38:50.403385-05	Assume college glass.\nState professor decision thus. Main lead eat case trial for half. Case some save.\nNatural worry plan claim. Wonder no carry which. However four difference report.\nOnce employee mind hit. News explain of pass no whatever.	168	545
1371	2018-12-21 14:38:50.409102-05	Hospital necessary close also them school. Soon bag up certainly drug add alone explain.\nRange night certain fly news model. Number eight over open. Meet brother go relate.\nShow time magazine audience morning decade.	23	547
1372	2018-12-21 14:38:50.417196-05	Become board save culture. Produce foreign control real dream although over.\nAllow wife Mrs just prevent available stay top. Be compare product leave. We price but very.	171	530
1373	2018-12-21 14:38:50.422737-05	Never road consider fall provide report. Heart brother then mean.\nPlant war build natural provide serious. Price pretty air.\nNew whatever change plan include. Everybody chance save concern figure hard develop.	171	539
1374	2018-12-21 14:38:50.428016-05	Sit painting art idea focus set. Structure all degree exactly.\nWeight drop he listen. Will customer figure expect throw meeting can.\nDiscussion citizen other must fact investment around. Consider see administration heart relate budget course.	167	509
1375	2018-12-21 14:38:50.435365-05	Person city play go bed although identify. Standard by despite method pass. Least head surface involve always buy.	169	535
1376	2018-12-21 14:38:50.441009-05	Report must style while though. Space report want body discover fine his.\nSocial reason material. Thousand player economic fast. East certain something material these.	173	512
1377	2018-12-21 14:38:50.446206-05	Trade likely blood dream practice town. Reach address serve similar water certainly say.\nOther employee finish defense art start. Series house different cause.\nBrother set each foreign life. Alone body tell reach.	173	509
1378	2018-12-21 14:38:50.452031-05	Like professor serious international here. Attack need stock coach require wrong.\nDiscover form argue little better. Student yourself less treatment board. Seek score area huge what force.\nStay standard character nothing. Hard on sport.	166	527
1379	2018-12-21 14:38:50.45725-05	No never detail. Particular behind structure maintain recently capital. A far skill bar leg knowledge.\nMajor religious forward describe which bill manager. Prepare significant home. Behind rock from word available.	159	545
1380	2018-12-21 14:38:50.463061-05	Could same benefit fund. Manage part world management site. Speech data occur population light special pay.\nSuddenly letter modern other Democrat scene nation student. Appear point activity try yard water.	175	504
1381	2018-12-21 14:38:50.47264-05	Ask light ability doctor. Ok weight land young. Own boy cold real customer near through.\nNow act executive author weight name. Never audience worker pass hour tree network.\nHour way someone data movie rock.	164	543
1382	2018-12-21 14:38:50.479857-05	Option carry TV.\nAgreement fast participant party serious say. School chair cut wind.\nDemocratic relate claim interest none art degree.\nMovie change politics however with. Ball answer return.	159	512
1383	2018-12-21 14:38:50.490533-05	Story assume last sing. Hard base partner take Mrs measure letter.\nAgent growth choice carry energy agency when. Remember various sport film single. Authority small financial sea require management threat.	169	541
1384	2018-12-21 14:38:50.499275-05	Whom unit central rock. Away interview especially structure sound arm imagine.\nReligious I put hold church budget information. Skill build score audience put.	172	516
1385	2018-12-21 14:38:50.512608-05	Goal future evidence. Door attention break. Soon song indeed executive offer. East decide physical drive describe.\nEnergy girl office give. Concern begin ball or.	162	542
1386	2018-12-21 14:38:50.52394-05	Back able live participant role course. Hour fight measure near approach same. What spend likely magazine best if.\nNetwork son use make section machine very office. Similar feeling enough economy one. Soon sing subject off boy.	165	518
1387	2018-12-21 14:38:50.529183-05	Popular never standard film claim improve. Security yourself few now wait rule approach. Military professor fear glass assume way structure.\nHour court stuff. Have threat him arm.	170	543
1388	2018-12-21 14:38:50.536677-05	Example explain wife skin forget. Fear page one notice. Pattern opportunity point wish direction citizen beautiful.\nWatch who end summer identify product. Building bank message operation item agent.	163	548
1389	2018-12-21 14:38:50.543019-05	Its police view detail everybody benefit value. Nature left rate moment summer. Table change hard question operation whom. Recently that born.\nWall seek mission off. Knowledge feeling fire system raise.	165	551
1390	2018-12-21 14:38:50.548206-05	Group rather car deep suddenly. Second available figure week just social lose wall. Ten describe check number exactly list recent. While of edge stage despite whose.	158	509
1391	2018-12-21 14:38:50.553686-05	Threat least clearly traditional give that interview community. Soldier majority fund. Stage low force owner woman security we car.\nEnd into tell evidence increase. Need play hundred organization.	162	525
1392	2018-12-21 14:38:50.55911-05	So education Mrs action claim set realize. Change perform social.\nProfessor be opportunity. Pm here remain think election leave role.\nSituation plan movie rule program ask interesting act. Cell despite close trade. See dream write baby late provide.	170	516
1393	2018-12-21 14:38:50.563943-05	Campaign great laugh begin none put food attention. Agent beyond boy focus thing.\nBoard score notice shoulder attorney. Performance not discover beautiful few relate road answer.	170	518
1394	2018-12-21 14:38:50.572991-05	Their medical later live career specific. Marriage daughter guess wife husband range all. Writer health position modern. Serious name adult inside.\nDrop structure risk. Many audience enjoy information.\nWhose together home.	165	523
1395	2018-12-21 14:38:50.578595-05	Figure who they until treatment traditional yourself lot.\nTonight goal cultural commercial little. Simple network push.\nApproach there career until. To kind between fast admit throughout can. Foreign region five phone lay education development.	169	537
1396	2018-12-21 14:38:50.5875-05	Region nothing total management small true clear mouth. Wife decade technology significant nature. Near outside yet staff item. Travel sort region life article.\nLow contain indicate. Company water stuff environment. Move her movie record.	172	544
1397	2018-12-21 14:38:50.592675-05	Deep official attention walk inside vote mouth. For per off continue.\nGround court mouth.\nThem moment two sometimes world four. Executive if matter direction baby. Rule environment dog benefit laugh help.	175	523
1398	2018-12-21 14:38:50.599929-05	Opportunity under how race sing southern. Join citizen born. Other hit when develop what. Success personal mind see whatever against despite.	170	550
1399	2018-12-21 14:38:50.606207-05	Base car war be training level join. Stuff director wrong few. Test about article success such what.\nMorning own ball goal drive reality prevent. It forward center space. Mention political firm trade commercial improve reach director.	169	538
1400	2018-12-21 14:38:50.611653-05	Watch late source call good most. Be night number avoid. Industry mission Mrs.\nLook low management at debate Mrs maintain will. Point share place great summer.	169	536
1401	2018-12-21 14:38:50.619637-05	Eye fly soldier leg street. Wrong painting idea bank picture.\nRoom particularly spend himself less. Leg box teacher after attack.\nFactor law what. Future least right how executive own fast. Somebody cause official deep.\nOld dog relate night.	173	544
1402	2018-12-21 14:38:50.627075-05	Run five others direction black listen make tonight. Fill step some source southern.\nAbove draw behavior against market. Participant similar direction fish. Whatever painting several certain without them painting red.	158	521
1403	2018-12-21 14:38:50.636865-05	Mention weight black lot pressure parent yourself. These choice account energy focus from. Four type room fire include. Forget series hand idea maintain three certainly.\nPicture court bed member finish. Clearly range choice identify.	158	523
1404	2018-12-21 14:38:50.642349-05	Eight law doctor teacher. Beat country everyone.\nSpend office save how. Until measure case measure same.\nForget career sound such. Know east feel she political throughout. Next third writer improve strong evidence expect.	166	518
1405	2018-12-21 14:38:50.647907-05	Song pull figure information anyone goal trade him. Economic maybe generation her even.\nPoint school establish he fish team although. Beyond poor may pull per. Gas everybody always act Democrat senior laugh cup.	164	544
1406	2018-12-21 14:38:50.656902-05	Late matter tell to long difficult. Southern fight only without group road throw.\nDemocratic stay evening news place own. Bit view Democrat. Deal bill marriage white wife customer.	163	552
1407	2018-12-21 14:38:50.662788-05	Table ask me picture. Leader audience city trial forget. Question early wrong various clear reach structure assume.\nRecent all threat action trouble brother. Cost record south describe.	171	519
1408	2018-12-21 14:38:50.67159-05	Only financial whatever opportunity. Fund dinner join level few.\nHow challenge difference send reflect. Range choose always message.\nJoin scene ground seem rich power deal. Him author without there number glass out condition.	170	534
1409	2018-12-21 14:38:50.677472-05	Safe never human picture. Power newspaper color high.\nScene identify or at. Chair those all show old. Six current resource.\nIndicate to tonight son sort term. Site style level moment production.	159	504
1410	2018-12-21 14:38:50.683579-05	Standard source positive first good year life international. Decade mean pretty rule modern.\nWatch grow each may produce successful along there.\nGrowth nation reduce floor social close. Pass grow body push seem.	161	511
1411	2018-12-21 14:38:50.69115-05	Beyond capital ok doctor ability ability. Score somebody friend today.\nOf with her successful safe decision feel. Other thousand enough respond simply marriage city well.	176	548
1412	2018-12-21 14:38:50.696932-05	Management floor physical today candidate audience relate. Race career professional yard but team.\nWhere business and hope reveal. So oil important body. Wonder chair rate general maybe director.	165	507
1413	2018-12-21 14:38:50.706351-05	Bed writer performance bill. Drive cup father major especially stage.\nListen successful how again five. Thank whose fact. Safe happy technology world reveal. Someone card movie role task.	165	516
1414	2018-12-21 14:38:50.712066-05	Ago detail prevent probably. Modern possible message thus may no rich. Customer television lot approach.\nYard form full include successful support night phone. Lead live trip.	159	514
1415	2018-12-21 14:38:50.720811-05	Read research area through he really space. Standard consider everything lose mention color. Friend north doctor.\nWife people wish or commercial. Purpose old go discussion notice each.\nReturn thing sometimes among necessary another suggest.	164	526
1416	2018-12-21 14:38:50.72615-05	Expert improve cup camera just quality big. Staff ago whatever have. If life lawyer enough course. Somebody check be them establish sort.\nStudent baby statement professor to north. Evidence reason support according.	176	547
1417	2018-12-21 14:38:50.731738-05	Assume likely drive page brother grow billion. Discussion visit father not not.\nHouse allow imagine break. Discussion guy good fact pressure.	173	517
1418	2018-12-21 14:38:50.741515-05	Nature energy research modern. Shake authority yourself drug.\nBeat TV difficult say peace meet. Ask very mention field management. Capital part spend also state forward.	160	508
1419	2018-12-21 14:38:50.749458-05	Hear test protect person financial. Kind management national involve old week medical. History phone when watch small order.\nThemselves personal interview scene school thousand. Perhaps market money next save.	23	515
1420	2018-12-21 14:38:50.758759-05	Environment bill evidence painting recently.\nReturn model that sound themselves. Issue ever off nearly job. Set focus city window.\nEnergy according help total probably. Forget paper style list fast art human.	162	543
1421	2018-12-21 14:38:50.764337-05	In although shake others condition. Professor own beautiful cover movement history. I interview anything low real six strategy among.\nNews whatever white rule. Station war hot ever from article garden.	164	538
1422	2018-12-21 14:38:50.773546-05	Push than film. Hotel could like large easy financial store our.\nBehavior party require candidate machine expect federal. Community behavior summer teach agency. Question save let wear happen possible within space. Son wait develop career he.	173	525
1423	2018-12-21 14:38:50.779335-05	Even list adult us provide house pull.\nHour image test let side leg. Offer approach recent style into seek between. Will wrong argue lot fact.	159	548
1424	2018-12-21 14:38:50.789945-05	Talk often minute long. Writer go religious expect activity short read. Ability place front possible against put. Success happen what.\nCity American perform action. Keep dark son around.	175	515
1425	2018-12-21 14:38:50.795888-05	Line president sister. Operation color meet modern.\nPolitical run admit write available. Evening leg ahead TV.\nSeek south wait thing young of crime. Office hard keep important huge use economy.	170	515
1426	2018-12-21 14:38:50.804989-05	Turn sure goal stop matter. Every above test focus scientist father. Imagine a agree option item.\nMr serve baby. Detail trip reflect image teacher.\nAgain point movement customer. Year likely tonight.	160	512
1427	2018-12-21 14:38:50.810954-05	Field debate television. Process big structure of join. Most agent bit maybe want good option.\nOnto generation she article campaign trouble possible smile.\nStop society happy trouble. Cost local answer enter lead across care carry.	163	524
1428	2018-12-21 14:38:50.817528-05	Walk figure there ready yes among. Tv free present president trade finally ahead. Major eat movement draw trial watch group model.\nArrive police operation fact. Direction speech treat care compare raise.	162	521
1429	2018-12-21 14:38:50.825837-05	Change light quality total believe structure bit. Sell control job west.\nLow nice though material. Paper think environment election local mouth.\nUse almost career on describe. Later work actually shoulder.	158	531
1430	2018-12-21 14:38:50.831676-05	Somebody put past anything people question American. Quality season attorney wonder everything year before. Six firm something author. Mother painting despite send north detail.	167	524
1431	2018-12-21 14:38:50.840328-05	Difficult strategy help weight in trade. Though speak crime choice agency stage gun.\nEconomy over serious coach improve half safe. Show meeting seven exist. Whose risk technology raise.	170	543
1432	2018-12-21 14:38:50.84609-05	Case pressure nearly reach major brother sense. Including school type research science today. Race interest financial other law market yet agent.\nTest important policy church bed serve. Recently could table officer radio.	164	551
1433	2018-12-21 14:38:50.855213-05	Though say what. Message true sound star. Season market huge smile treatment live friend.\nWhile recently foreign factor hour run black. Like near travel Mrs organization main because. Long order national watch indicate thousand.	168	523
1434	2018-12-21 14:38:50.863322-05	Allow student course like gas power size. Value walk run answer.\nLess product before least along position whose. As interview run else. Range notice staff game argue decide.	174	506
1435	2018-12-21 14:38:50.873597-05	Yet staff production sell trouble. Maintain include capital people respond hear kid. Back thousand local affect.\nWin even eight better television modern. Than impact all book body series.\nThan college risk lawyer kid.	174	529
1436	2018-12-21 14:38:50.879662-05	Out into report carry. Republican least peace above piece join.\nTime receive even consumer. Themselves read energy operation camera. Focus dog develop network court.\nRange operation decision ever force cultural. Hundred business thus that nothing.	161	544
1437	2018-12-21 14:38:50.889621-05	Book put least source lead suffer. Evening authority find. Protect return understand specific well avoid turn teacher.\nShould health any over sea appear present. Find matter artist lose. Friend dog most head short remain.	23	511
1438	2018-12-21 14:38:50.894885-05	Property his type score movement. Mouth less environmental participant sort beyond. New more item suffer edge while.\nForward media traditional whether. Arrive level down near person sure memory. Difference especially receive toward light during.	168	539
1439	2018-12-21 14:38:50.902442-05	Who yourself summer worker. Much several often. Way population body during. Attention be again question big painting.\nStudy beyond reflect test pressure product. Tree style behind plan center.	170	538
1440	2018-12-21 14:38:50.909338-05	Hold culture occur paper. Republican type ok. Sing another third suffer. Dream conference technology seem.\nLook probably once program. Build edge huge build statement. Must picture company want remain wrong.	176	506
1441	2018-12-21 14:38:50.914999-05	Brother drop class military tonight set. Until believe TV service pass stock both. Character prove game chair his ball fish.\nWhich picture soon. News population to. Develop successful wide culture. Home two interesting particularly.	168	520
1442	2018-12-21 14:38:50.920255-05	Law world ask outside. Side two thousand. Billion word model commercial feeling join strategy.\nShe hear require manager available whom green. Property interview have.	162	547
1443	2018-12-21 14:38:50.925513-05	Sort news staff kid final finally move special. Off along six general. Do so nearly lay.\nIdentify answer choose drop outside hospital just. Hold final clear memory treat. Medical sense seven.\nFinancial threat true. Get training impact money.	166	532
1444	2018-12-21 14:38:50.930557-05	By office inside memory item. Understand member fire discussion decade expect. Safe someone like threat.\nSite black those just system keep add. Lay wish now government also political.\nGeneral measure entire perhaps.	175	551
1445	2018-12-21 14:38:50.939105-05	Fall that cut color relationship worker industry. Hair off story wear side current factor.\nMedical since law society continue alone market. Focus process cut certain owner center. Place fill than impact memory usually.	161	521
1446	2018-12-21 14:38:50.944692-05	Almost person must nothing agency father almost. Apply in identify already.\nIdea life land her series. Coach speak professional here message.\nTrial road inside similar act student.	164	504
1447	2018-12-21 14:38:50.951897-05	Glass sound day paper. Identify together with hand response foot.\nArticle expert truth million rich today bring. Sit actually seat front. Property end game approach quickly mention edge sometimes. Late property rate from political bill.	167	514
1448	2018-12-21 14:38:50.957463-05	Statement five federal key. Fine soon environment shoulder near strategy. Allow both way gas.\nFloor land deal part. Discover man one eight.\nOrganization service bar information. Idea someone century region similar rate.	165	547
1449	2018-12-21 14:38:50.96303-05	Fine course science man research. Yes boy attention join.\nUsually lead low. Have get history already six win field painting.\nFill notice poor education practice grow increase. Meet pattern unit wife.	160	511
1450	2018-12-21 14:38:50.969603-05	None program official believe suggest stock young. Last plan sit. Poor list forward above method.\nTrial happy audience international. Number argue within culture yes next occur. Senior change society artist method likely.	162	514
1451	2018-12-21 14:38:50.975349-05	Population challenge begin eye recognize common available. Story great from hand series. Push send under somebody woman strong.\nTrial yourself when fire. Message with treatment heavy sing.	160	544
1452	2018-12-21 14:38:50.982248-05	Exist end fine manage court special. Bar nation line amount security later.\nEstablish cup financial drug practice night.\nBest hospital look as. Ago public choose statement.	170	519
1453	2018-12-21 14:38:50.991381-05	Someone network me heart.\nOccur example dream usually interest.\nRace movement price build image. Also discuss officer until quite. Foreign economic time administration top body only.	171	532
1454	2018-12-21 14:38:50.997017-05	Cell available positive meet base group. Hold media trial.\nTreat difficult into girl.\nMiddle memory run money manage these. Deep market art summer data certain. National pressure whatever final kind year huge.	164	508
1455	2018-12-21 14:38:51.005511-05	Avoid before suggest bar. Born upon save give surface. Require power prove wife today agent.\nLive information especially hold manage. House Republican traditional shoulder book thing. Relate beat until director very.	171	518
1456	2018-12-21 14:38:51.01101-05	Special me out single. Industry which pattern time. Attention win role pressure take stage.\nGive until perform same. Citizen front lead form sometimes film toward. Maybe art indicate size second behavior discussion work.	165	514
1457	2018-12-21 14:38:51.016705-05	Nor sister raise. Site more never guess.\nDevelop watch bar. Camera opportunity reduce evening campaign media. Air smile paper affect draw between develop.\nBetween class staff good physical organization. Center board half dark weight. Cover all that.	172	515
1458	2018-12-21 14:38:51.02515-05	Top heart natural fill. Early build off wrong speech reveal. Type whole receive top professional full list. Choice meeting organization modern.\nStage people else less artist experience model.	176	536
1459	2018-12-21 14:38:51.030966-05	Yard theory image season long. Hard range cold.\nFirst collection head fine. Woman become seat another.\nMovement kind prevent draw conference. General discuss other do. National response toward matter happen rock positive.	162	541
1460	2018-12-21 14:38:51.039163-05	Conference her population meet hit need future use. Stuff place evening ok poor a. Your floor us goal general key type.	167	504
1461	2018-12-21 14:38:51.044764-05	Appear water recognize when focus. Single detail car new argue son. Poor production upon yourself.\nTreat change American far. Industry charge despite former figure cost animal.\nCultural only authority score around what find.	165	516
1462	2018-12-21 14:38:51.05016-05	Myself wide poor involve occur toward.\nTraditional story animal son several hand. Give somebody air author draw involve news. Image between traditional.	163	531
1463	2018-12-21 14:38:51.058335-05	Fish spring one point job including. Into avoid laugh scientist chair sort. Population hope now white buy feeling.\nJoin perhaps color town identify upon occur. Million those of base adult quickly agreement way.	162	525
1464	2018-12-21 14:38:51.063675-05	Two never deal probably professor. Positive give across mention radio control ground education. Time season eight operation.\nPublic show whole million color authority. Rate student example task.	166	544
1465	2018-12-21 14:38:51.071938-05	Customer its rest family toward cost two week. Next reflect whom politics page whom. Leg citizen project join network try.\nAgainst ten late give. Similar attorney factor television painting hope specific. Discuss worry side indicate already.	23	503
1466	2018-12-21 14:38:51.077468-05	Later board nearly other central. True once dinner.\nStore star art red too.\nSimply might purpose situation. Or special around and. Bed term yes reality protect skin firm right.	23	520
1467	2018-12-21 14:38:51.083545-05	Kid my sound sport land specific. These subject and wear military surface. She common place.\nDifficult wonder sense herself report trade. Employee lawyer task finish suggest class.	165	527
1468	2018-12-21 14:38:51.092377-05	Film sure common cultural weight popular significant. Sure best serve improve catch. American pressure radio Mrs successful wait.	169	505
1469	2018-12-21 14:38:51.100533-05	Government check base purpose. Financial change Mrs eat team job everything. Process himself score usually.\nStudy administration admit author respond. Through really skill customer true. Road capital any.	160	545
1470	2018-12-21 14:38:51.109984-05	Someone maybe music. Start radio treatment interview choose term let sport.\nPosition growth agree. Voice person body poor radio. Establish off along guess data single mission.	163	521
1471	2018-12-21 14:38:51.115998-05	Clear blue eat trade book. Allow doctor visit civil key.\nListen writer young marriage. Organization commercial collection body result low.\nIndustry yourself somebody friend. Their as economy during hard stay forget.	161	530
1472	2018-12-21 14:38:51.124664-05	Several consumer candidate sense pull agent wear. Crime step bit until popular time.	166	528
1473	2018-12-21 14:38:51.130344-05	Her news industry special hold instead lay. Beat him feel add health fine. Draw grow produce region.\nAnother deal low professor general wonder figure. Concern someone eat item theory heart order much. Yet too husband material purpose feel someone.	165	550
1474	2018-12-21 14:38:51.138912-05	Range as member him. Quality door spring which clear. Economy meet probably standard serious discuss building continue.\nProperty phone field. Piece front everybody coach. Development deep fill lose. Wide fish still prove election factor.	163	545
1475	2018-12-21 14:38:51.145481-05	Series development fall international cost difficult. Only yet truth ground economy. Beautiful through main keep lay.	159	539
1476	2018-12-21 14:38:51.15589-05	Itself feel plan still recently.\nFear join leader. Future will white capital right. Work range allow job term.	165	523
1477	2018-12-21 14:38:51.162508-05	Too water fire edge tough surface hope. Memory spend to the man market season.\nThought direction later fund event market. Month trial wide behind.\nNow recent line. Dark old between through. Very nor anyone south cause lot anything.	173	536
1478	2018-12-21 14:38:51.171415-05	Carry father eye remain term. Note phone professional strong knowledge national thing assume. Road interest about past.\nInvestment religious structure clearly dinner woman. General may age market. Window whether great foreign leave.	23	538
1479	2018-12-21 14:38:51.177428-05	Of test successful collection create daughter. Within direction word citizen. Campaign employee camera.\nWay scene among scientist.\nGrowth second move care. Sure system form around second store various. Reason sign world as site.	172	508
1480	2018-12-21 14:38:51.183317-05	Kid book resource carry. For tend house beyond partner woman. Manage home partner against social past me.\nThan part family realize. Anything month heart general can.\nConsider six just we guess available. Toward investment middle consumer yard.	159	520
1481	2018-12-21 14:38:51.192071-05	Marriage tough foot success end month bag treat. Other behavior home time.\nView issue thought fall.\nLawyer there young woman alone attorney. Matter without specific. Within official apply president film hold win.	164	545
1482	2018-12-21 14:38:51.198507-05	Quality view thing. Especially price away dog three. Cup he democratic politics attack factor really.\nEspecially general first strategy seek. Main law hit hold usually experience. Note without out other campaign necessary stay sea.	162	509
1483	2018-12-21 14:38:51.207436-05	Claim include see business. Company now interesting generation.\nCup section might just discussion course. Must anything listen peace. Go picture hospital. As rock meet build computer training nation.\nWish quite spend especially where.	173	506
1484	2018-12-21 14:38:51.213656-05	Clear lawyer on not without tough war. Fire size camera international budget suggest. About economy state bank business.\nHand hit girl free. Tonight seek view continue add score. Sort newspaper place network represent.	175	551
1485	2018-12-21 14:38:51.224407-05	Star mother these whatever treat. Size management kind fear commercial.\nAdd because matter focus man well person soon.\nMove necessary cut PM later role get. Local admit cover rock scene. Develop compare though the rest.	176	503
1486	2018-12-21 14:38:51.23148-05	Cold although Mr move manager. Day oil understand respond result. Attorney list meet the scene.\nArtist TV media past write. Tree job air picture environment.	164	522
1487	2018-12-21 14:38:51.2371-05	Girl face care establish ago pull smile. Church land investment suddenly education partner accept work.\nReach government too try single least improve red. Listen range role item peace off.	167	537
1488	2018-12-21 14:38:51.243544-05	Discussion picture lead recently economy today tell. Trouble wait protect company power manage senior choice.\nKnow learn drop drop affect role. Rather reduce teach mother within. Maybe marriage us they around put memory.	176	539
1489	2018-12-21 14:38:51.249204-05	Movement strong note leave talk. Which push early. Gun body yeah these short manage financial real.\nSpring fish room tell which response pressure. Civil range about record build. Single successful evening wear provide majority paper.	171	526
1490	2018-12-21 14:38:51.257217-05	Game life not foreign various size. Central reach million watch PM rate.\nRead yeah debate prove main. Down one writer alone whatever along.	172	552
1491	2018-12-21 14:38:51.262784-05	Attention cover environment book just. Ground cut address property recognize treat indeed. Other push dinner amount hot such responsibility.\nJoin century new past anyone. They continue before oil stock great pay.	167	511
1492	2018-12-21 14:38:51.270849-05	Quite similar strong perform. Place probably space my. Personal treatment read tough ready establish government.\nThat collection hundred professional high. Product from tax adult.\nArm skill both change natural treatment draw.	169	522
1493	2018-12-21 14:38:51.276011-05	Mission travel to certainly American. If article value glass pay family. Myself option by pass law.	162	530
1494	2018-12-21 14:38:51.281447-05	Bank drop enjoy her. Agreement art relationship a view fine.\nEarly may front suffer result trouble trial. Benefit last team form away quality television. Foreign site dog center structure give though.	23	521
1495	2018-12-21 14:38:51.28982-05	Amount somebody goal score kitchen billion finally. Because three information must gas. Method specific especially door everybody.\nLarge treat spring want sell cover. Trip story military marriage begin enter. List well however.	23	507
1496	2018-12-21 14:38:51.295278-05	Different analysis behind Mr. Land college PM reason practice young. Feel security source because start bank already against.	166	544
1497	2018-12-21 14:38:51.301984-05	Thing help dinner huge. Speak peace best pick.\nGoal maybe include left kind. Matter anyone also card employee politics carry put.\nBeautiful reveal call such already while. Bag huge seven generation how boy.	164	544
1498	2018-12-21 14:38:51.309125-05	Enjoy character particular. Exist book heavy design. Visit last war movie. Accept hand open operation approach deal stay thousand.\nTonight goal either whether myself young. Fall read guy treat none everybody local. Claim event half staff.	23	522
1499	2018-12-21 14:38:51.314701-05	Letter next place range share event factor. Technology have treatment dog federal. Some environment each improve will.\nDecide street west cold speak. Play garden Republican become Mrs. Truth leave eat take star.	162	543
1500	2018-12-21 14:38:51.323396-05	Plant fire Republican product fire enough. Western attack entire yes every. List either personal above indeed current condition.\nWall him physical within. Sit bill recent nor food issue seat.	159	526
1501	2018-12-21 14:38:51.329125-05	Character culture table before. Hotel resource pay price himself clear talk.\nNone method TV record much. Discuss as education wind. Cut religious tend be my head.	173	544
1502	2018-12-21 14:38:51.339283-05	Woman need oil series out too condition your. Number believe finish bar actually.\nRadio respond happen research teacher certainly. Minute professor event describe establish. Name shake war among.	166	525
1503	2018-12-21 14:38:51.34601-05	Though respond make choice simply without father. Compare toward picture future mind discuss.\nCertain success adult model want. Hear act structure house foot age size. International white alone feeling.	162	533
\.


--
-- Data for Name: questions_profile; Type: TABLE DATA; Schema: public; Owner: questionbox
--

COPY public.questions_profile (id, image, user_id) FROM stdin;
\.


--
-- Data for Name: questions_question; Type: TABLE DATA; Schema: public; Owner: questionbox
--

COPY public.questions_question (id, created_at, title, text, author_id) FROM stdin;
503	2018-12-21 14:38:50.018853-05	Test Question 0	Of west detail note. Fast stop member traditional probably. Pressure on contain other upon effect key.\nIndicate health dark other. Physical everybody along after religious court major.	175
504	2018-12-21 14:38:50.022713-05	Test Question 1	Technology measure dream explain market tend speak. Night feel garden data make new policy. Walk near eye person.\nSerious onto sometimes difficult amount film themselves. Hear decide sound feel.	170
505	2018-12-21 14:38:50.026108-05	Test Question 2	Training practice against speech office cultural. Spend contain pull painting two hold improve strong. Section leave industry.	173
506	2018-12-21 14:38:50.031772-05	Test Question 3	Scientist three catch trial strong. But behavior although baby field common.\nHead here everybody red east. Call ball benefit among break stand.	176
507	2018-12-21 14:38:50.037639-05	Test Question 4	Grow how expect over gun any now sell. Down other small raise will discover medical.\nFor behind herself read deal save wear.	163
508	2018-12-21 14:38:50.041329-05	Test Question 5	Call compare dream whose. Actually cut thousand available.\nGood game much.\nTreatment same provide investment call may.\nMaterial significant high pull appear challenge network. Challenge baby always government wind white.	176
509	2018-12-21 14:38:50.046743-05	Test Question 6	Memory where state build. Pretty doctor remain from long head.\nService specific always as both. Think indicate shake mean involve poor stop.	166
510	2018-12-21 14:38:50.05003-05	Test Question 7	World pretty mention create occur hold pay. Smile among surface myself recently.\nDefense fire article break factor add. Mission teach article husband record firm measure.	162
511	2018-12-21 14:38:50.053667-05	Test Question 8	Financial fight talk director energy much probably. Series always front what degree perhaps clearly. We career TV by machine police thank.	166
512	2018-12-21 14:38:50.057046-05	Test Question 9	Now I away moment money.\nBefore drive return rate he keep begin. Movie source garden. Own dog avoid street if standard free. Trouble next education property under.	164
513	2018-12-21 14:38:50.060616-05	Test Question 10	Experience save bed maintain. Across different five heart bring bad data.\nBad indicate order. Hit student case up charge wonder.	165
514	2018-12-21 14:38:50.066198-05	Test Question 11	Individual senior skin before must just full. Spend trouble body. Indeed kid reason while help.\nBut yeah small every. Stock condition pretty son idea finally within girl.	158
515	2018-12-21 14:38:50.069846-05	Test Question 12	Your woman television crime police wide here. Ok myself image collection. Decade analysis return drug nation.\nEdge trade fast piece fast. South relate painting skill.	163
516	2018-12-21 14:38:50.073384-05	Test Question 13	Against street ball American. Play event certainly tough player.\nBetter fear by thousand either. Deal main almost.\nProperty including relationship throughout. Stage who wind full speech others poor.	162
517	2018-12-21 14:38:50.077392-05	Test Question 14	Road capital item size morning check. Force any it stock pressure. Read magazine individual employee now campaign.\nThousand job oil radio national per Mr. Space group talk top us magazine field. Wonder often back.	164
518	2018-12-21 14:38:50.082945-05	Test Question 15	Investment rather new kind couple last big. Million miss traditional compare. Top follow race.\nHow foot protect let large lot. Key remember future protect help mind entire.	164
519	2018-12-21 14:38:50.086698-05	Test Question 16	Health inside board health often example.\nBoth owner nature character. Coach field alone.\nAccording off language expect whether visit.	176
520	2018-12-21 14:38:50.090128-05	Test Question 17	Someone sort join social player trouble. Dark girl eat.\nShake among run health stop admit act. Customer manager including step all may figure. Matter send performance. Film trouble who you reflect modern star.	158
521	2018-12-21 14:38:50.094034-05	Test Question 18	Ok big certain. By company choice research about. Actually Democrat shoulder her simply not degree.\nPrice picture tree throughout product great special cover. Teach wonder because natural difference machine final.	165
522	2018-12-21 14:38:50.10012-05	Test Question 19	Follow entire almost. Save present red policy drive. Little many military professional across another. Next writer win include sell.\nResearch wife interesting sell increase.	166
523	2018-12-21 14:38:50.103811-05	Test Question 20	Someone toward consider set hair year. Daughter official kind more practice thing. Executive lose clear take back perform.	160
524	2018-12-21 14:38:50.107679-05	Test Question 21	Subject laugh raise suddenly value perhaps environmental. Daughter tax wrong success bag party good. Result beautiful interview lawyer live whole.	167
525	2018-12-21 14:38:50.111399-05	Test Question 22	Yet later political wrong. Happy create blue age after buy must.\nRisk can clear lawyer wear. Tree group move however. Like impact place figure project develop dream allow. Past economic help writer.	164
526	2018-12-21 14:38:50.117359-05	Test Question 23	Nature develop wish test film and ready. Pass accept middle appear attention. Trip drop fight.\nDevelopment sell item pass. Chair under group career show side. Bag find agency person something drug.	175
527	2018-12-21 14:38:50.121153-05	Test Question 24	Allow own radio onto next it writer. American say particularly important word should.\nMain name general computer hand billion. Nearly tend sign bring. Million guy assume whose.\nGoal social happen door middle those.	171
528	2018-12-21 14:38:50.124563-05	Test Question 25	Fast company full phone.\nAgreement listen his agreement. Hour quickly near later eat.\nTeach go painting environment. Teach turn model continue.	169
529	2018-12-21 14:38:50.129344-05	Test Question 26	Son focus easy personal me check. Source half budget reality care far serve. Foreign century bar type.	158
530	2018-12-21 14:38:50.134179-05	Test Question 27	In wonder least do base. Artist central bill south avoid health story. Chair standard one.\nDecade argue low final floor report fish. Financial economy book play measure feel art arrive. Land crime artist draw new phone.	168
531	2018-12-21 14:38:50.13813-05	Test Question 28	Central culture beat important possible reveal one worry.\nMatter return create teach section necessary.	168
532	2018-12-21 14:38:50.141668-05	Test Question 29	Western fight cold leader wait training. Set beat tend create right value. Physical color likely rise computer moment much. Way space shake modern ability thing south.	162
533	2018-12-21 14:38:50.145095-05	Test Question 30	Process floor business someone Democrat doctor chair. Music number billion certainly small. Significant scientist apply information start. Health skin current process close any.	163
534	2018-12-21 14:38:50.148905-05	Test Question 31	Wear speak raise ready piece heart growth office. Oil born wide mouth hear everybody. Audience bill poor sort.\nNearly teacher tend. Support suddenly under husband close himself. Difference too high produce hope.	169
535	2018-12-21 14:38:50.155663-05	Test Question 32	From allow minute somebody far like. Friend especially well fly scientist war.\nImagine order chance information region other tree box. Attack discover including yourself.	162
536	2018-12-21 14:38:50.198452-05	Test Question 33	Feel eye hour show lead until themselves. White minute especially successful.\nWrite meet house soldier painting anyone. Office much technology. Hold parent fish age significant institution choice total.	161
537	2018-12-21 14:38:50.202296-05	Test Question 34	Answer way report fire suggest together sure agree. Year avoid prove risk move open.\nStore watch care. Just case pretty event put. Place teach admit many development really total.\nRepublican sound general girl.	171
538	2018-12-21 14:38:50.207216-05	Test Question 35	Sing add behavior house.\nBillion either she rest above staff. Leave one small week standard owner.\nGirl tree class act history watch. Term wrong tend hair.\nLike development learn local here main. Measure guess plan pretty.	160
539	2018-12-21 14:38:50.211298-05	Test Question 36	Figure themselves shake baby law talk. Land reason air stuff clear rich.\nBag big several wind just. Interesting animal wonder suffer. Foreign just million positive.	165
540	2018-12-21 14:38:50.215392-05	Test Question 37	More work though keep. Attack former thought blue suddenly now space. Visit special the defense.\nNow subject instead camera play property. Sit difficult spend eat visit piece.	23
541	2018-12-21 14:38:50.219966-05	Test Question 38	Interest five answer difficult your option. Financial term my chair someone remember. Lead energy everyone both lead.\nYoung ask beat energy show represent step.\nSupport baby act. Report relate account hard most.	161
542	2018-12-21 14:38:50.223458-05	Test Question 39	Big tough maintain process business story others prove. Long draw executive chance color care someone. Health American between toward suffer medical behind.	176
543	2018-12-21 14:38:50.228391-05	Test Question 40	As recognize make join hot may. You situation official concern medical.\nOn until expect away agent. Every reach degree into story knowledge court. Feeling town even future should business set.	169
544	2018-12-21 14:38:50.23472-05	Test Question 41	Argue career his we remember. End against almost reach. Travel much newspaper career task charge.\nAway modern happen happy.\nRecognize seem set degree. White alone despite senior.	175
545	2018-12-21 14:38:50.238979-05	Test Question 42	Low charge join technology night brother front. Represent direction stay five.\nSecurity mention include citizen chair safe stuff. Anything again determine top hotel factor. Commercial white last thus friend.	174
546	2018-12-21 14:38:50.242834-05	Test Question 43	Capital tend raise responsibility time argue pull.\nDirector dark easy page age national official. Week society leg couple.\nSimilar modern place computer. Woman turn way fine follow involve data.	162
547	2018-12-21 14:38:50.250847-05	Test Question 44	Agree own finally. Last human nice significant lot my husband. Us reality present north prevent glass firm.\nStop away artist where hundred space. Charge certain offer use. Chance born she mean.	158
548	2018-12-21 14:38:50.256987-05	Test Question 45	Thank health I around book house. Ok that approach consider. Store fight manage others to including.\nMother ok investment special. Pick like push simply station first. None beautiful another.	159
549	2018-12-21 14:38:50.260701-05	Test Question 46	Threat know little top. Pattern manager man name phone final accept. Partner at nearly wrong mouth.\nYet recognize often day state ground break. Not it lot blood.	163
550	2018-12-21 14:38:50.267702-05	Test Question 47	Save specific enough shake. Artist reveal feeling way ahead agreement. Many letter enter current then assume second.\nOff single piece moment eye hour structure. Close toward wish federal surface prove trial.	164
551	2018-12-21 14:38:50.272507-05	Test Question 48	By forward minute information. Father either campaign concern left girl apply.\nIncrease relate answer. Can stage might receive mouth everyone speech feeling.	163
552	2018-12-21 14:38:50.28558-05	Test Question 49	Understand low up tree computer these. Result nice option apply pattern herself lawyer.\nSound above daughter gun road total. Specific character avoid. Always worker affect say religious simple often town.	158
\.


--
-- Data for Name: questions_starreditem; Type: TABLE DATA; Schema: public; Owner: questionbox
--

COPY public.questions_starreditem (id, object_id, content_type_id, user_id) FROM stdin;
44	503	8	23
45	504	8	23
\.


--
-- Data for Name: questions_user; Type: TABLE DATA; Schema: public; Owner: questionbox
--

COPY public.questions_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
23	pbkdf2_sha256$120000$WN933S1VwJvD$7m8yuxmIOq7A7lb6ek9gRBBc5HNQ3bsdCETXsCFfNfs=	2018-12-21 14:00:33.495626-05	t	fan			fan.huang.33@gmail.com	t	t	2018-12-19 09:13:09.321676-05
158	quizme(11)	\N	f	Carrie.Trevino			Carrie.Trevino@test.com	f	t	2018-12-21 14:38:49.983281-05
159	quizme(11)	\N	f	Taylor.Scott			Taylor.Scott@test.com	f	t	2018-12-21 14:38:49.985644-05
160	quizme(11)	\N	f	Mary.Hunt			Mary.Hunt@test.com	f	t	2018-12-21 14:38:49.987169-05
161	quizme(11)	\N	f	Harold.Burgess			Harold.Burgess@test.com	f	t	2018-12-21 14:38:49.988596-05
162	quizme(11)	\N	f	Angela.Fletcher			Angela.Fletcher@test.com	f	t	2018-12-21 14:38:49.990041-05
163	quizme(11)	\N	f	Jeffrey.Hill			Jeffrey.Hill@test.com	f	t	2018-12-21 14:38:49.991467-05
164	quizme(11)	\N	f	April.Hernandez			April.Hernandez@test.com	f	t	2018-12-21 14:38:49.992936-05
165	quizme(11)	\N	f	Sheri.Wright			Sheri.Wright@test.com	f	t	2018-12-21 14:38:49.994396-05
166	quizme(11)	\N	f	Christine.Lopez			Christine.Lopez@test.com	f	t	2018-12-21 14:38:49.995996-05
167	quizme(11)	\N	f	Wayne.Vance			Wayne.Vance@test.com	f	t	2018-12-21 14:38:49.99743-05
168	quizme(11)	\N	f	Troy.Coleman			Troy.Coleman@test.com	f	t	2018-12-21 14:38:49.998822-05
169	quizme(11)	\N	f	Dr..Holly.Greene.MD			Dr..Holly.Greene.MD@test.com	f	t	2018-12-21 14:38:50.000292-05
170	quizme(11)	\N	f	Kristin.Escobar			Kristin.Escobar@test.com	f	t	2018-12-21 14:38:50.001863-05
171	quizme(11)	\N	f	Brian.Williams			Brian.Williams@test.com	f	t	2018-12-21 14:38:50.003327-05
172	quizme(11)	\N	f	Brenda.Cobb			Brenda.Cobb@test.com	f	t	2018-12-21 14:38:50.00478-05
173	quizme(11)	\N	f	Albert.Lopez			Albert.Lopez@test.com	f	t	2018-12-21 14:38:50.006285-05
174	quizme(11)	\N	f	Robert.Warner			Robert.Warner@test.com	f	t	2018-12-21 14:38:50.00795-05
175	quizme(11)	\N	f	Rebecca.Taylor			Rebecca.Taylor@test.com	f	t	2018-12-21 14:38:50.009421-05
176	quizme(11)	\N	f	Michael.Cooper.Jr.			Michael.Cooper.Jr.@test.com	f	t	2018-12-21 14:38:50.011094-05
177	pbkdf2_sha256$120000$K7peWzaJqm8V$+t0aJOf5gOTVRdDJs1FHDF/jSZcKYycTr1zmrRYaK8w=	\N	t	fan2			fan.huang.33@gmail.com	t	t	2018-12-21 14:39:26.849216-05
\.


--
-- Data for Name: questions_user_groups; Type: TABLE DATA; Schema: public; Owner: questionbox
--

COPY public.questions_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: questions_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: questionbox
--

COPY public.questions_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: registration_registrationprofile; Type: TABLE DATA; Schema: public; Owner: questionbox
--

COPY public.registration_registrationprofile (id, activation_key, user_id, activated) FROM stdin;
\.


--
-- Data for Name: registration_supervisedregistrationprofile; Type: TABLE DATA; Schema: public; Owner: questionbox
--

COPY public.registration_supervisedregistrationprofile (registrationprofile_ptr_id) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: questionbox
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: questionbox
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: questionbox
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 52, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: questionbox
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 28, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: questionbox
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 13, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: questionbox
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 26, true);


--
-- Name: questions_answer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: questionbox
--

SELECT pg_catalog.setval('public.questions_answer_id_seq', 1503, true);


--
-- Name: questions_profile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: questionbox
--

SELECT pg_catalog.setval('public.questions_profile_id_seq', 1, false);


--
-- Name: questions_question_id_seq; Type: SEQUENCE SET; Schema: public; Owner: questionbox
--

SELECT pg_catalog.setval('public.questions_question_id_seq', 552, true);


--
-- Name: questions_starreditem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: questionbox
--

SELECT pg_catalog.setval('public.questions_starreditem_id_seq', 45, true);


--
-- Name: questions_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: questionbox
--

SELECT pg_catalog.setval('public.questions_user_groups_id_seq', 1, false);


--
-- Name: questions_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: questionbox
--

SELECT pg_catalog.setval('public.questions_user_id_seq', 177, true);


--
-- Name: questions_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: questionbox
--

SELECT pg_catalog.setval('public.questions_user_user_permissions_id_seq', 1, false);


--
-- Name: registration_registrationprofile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: questionbox
--

SELECT pg_catalog.setval('public.registration_registrationprofile_id_seq', 1, false);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: authtoken_token authtoken_token_pkey; Type: CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_pkey PRIMARY KEY (key);


--
-- Name: authtoken_token authtoken_token_user_id_key; Type: CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_key UNIQUE (user_id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: questions_answer questions_answer_pkey; Type: CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.questions_answer
    ADD CONSTRAINT questions_answer_pkey PRIMARY KEY (id);


--
-- Name: questions_profile questions_profile_pkey; Type: CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.questions_profile
    ADD CONSTRAINT questions_profile_pkey PRIMARY KEY (id);


--
-- Name: questions_profile questions_profile_user_id_key; Type: CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.questions_profile
    ADD CONSTRAINT questions_profile_user_id_key UNIQUE (user_id);


--
-- Name: questions_question questions_question_pkey; Type: CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.questions_question
    ADD CONSTRAINT questions_question_pkey PRIMARY KEY (id);


--
-- Name: questions_starreditem questions_starreditem_pkey; Type: CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.questions_starreditem
    ADD CONSTRAINT questions_starreditem_pkey PRIMARY KEY (id);


--
-- Name: questions_starreditem questions_starreditem_user_id_object_id_conten_2145dabc_uniq; Type: CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.questions_starreditem
    ADD CONSTRAINT questions_starreditem_user_id_object_id_conten_2145dabc_uniq UNIQUE (user_id, object_id, content_type_id);


--
-- Name: questions_user_groups questions_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.questions_user_groups
    ADD CONSTRAINT questions_user_groups_pkey PRIMARY KEY (id);


--
-- Name: questions_user_groups questions_user_groups_user_id_group_id_580ab3d0_uniq; Type: CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.questions_user_groups
    ADD CONSTRAINT questions_user_groups_user_id_group_id_580ab3d0_uniq UNIQUE (user_id, group_id);


--
-- Name: questions_user questions_user_pkey; Type: CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.questions_user
    ADD CONSTRAINT questions_user_pkey PRIMARY KEY (id);


--
-- Name: questions_user_user_permissions questions_user_user_perm_user_id_permission_id_40df9c10_uniq; Type: CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.questions_user_user_permissions
    ADD CONSTRAINT questions_user_user_perm_user_id_permission_id_40df9c10_uniq UNIQUE (user_id, permission_id);


--
-- Name: questions_user_user_permissions questions_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.questions_user_user_permissions
    ADD CONSTRAINT questions_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: questions_user questions_user_username_key; Type: CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.questions_user
    ADD CONSTRAINT questions_user_username_key UNIQUE (username);


--
-- Name: registration_registrationprofile registration_registrationprofile_pkey; Type: CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.registration_registrationprofile
    ADD CONSTRAINT registration_registrationprofile_pkey PRIMARY KEY (id);


--
-- Name: registration_registrationprofile registration_registrationprofile_user_id_key; Type: CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.registration_registrationprofile
    ADD CONSTRAINT registration_registrationprofile_user_id_key UNIQUE (user_id);


--
-- Name: registration_supervisedregistrationprofile registration_supervisedregistrationprofile_pkey; Type: CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.registration_supervisedregistrationprofile
    ADD CONSTRAINT registration_supervisedregistrationprofile_pkey PRIMARY KEY (registrationprofile_ptr_id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: questionbox
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: questionbox
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: questionbox
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: questionbox
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: authtoken_token_key_10f0b77e_like; Type: INDEX; Schema: public; Owner: questionbox
--

CREATE INDEX authtoken_token_key_10f0b77e_like ON public.authtoken_token USING btree (key varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: questionbox
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: questionbox
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: questionbox
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: questionbox
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: questions_answer_author_id_ceb2e333; Type: INDEX; Schema: public; Owner: questionbox
--

CREATE INDEX questions_answer_author_id_ceb2e333 ON public.questions_answer USING btree (author_id);


--
-- Name: questions_answer_question_id_45884d67; Type: INDEX; Schema: public; Owner: questionbox
--

CREATE INDEX questions_answer_question_id_45884d67 ON public.questions_answer USING btree (question_id);


--
-- Name: questions_question_author_id_f53392d1; Type: INDEX; Schema: public; Owner: questionbox
--

CREATE INDEX questions_question_author_id_f53392d1 ON public.questions_question USING btree (author_id);


--
-- Name: questions_starreditem_content_type_id_87569512; Type: INDEX; Schema: public; Owner: questionbox
--

CREATE INDEX questions_starreditem_content_type_id_87569512 ON public.questions_starreditem USING btree (content_type_id);


--
-- Name: questions_starreditem_user_id_cc32ed93; Type: INDEX; Schema: public; Owner: questionbox
--

CREATE INDEX questions_starreditem_user_id_cc32ed93 ON public.questions_starreditem USING btree (user_id);


--
-- Name: questions_user_groups_group_id_e02b4060; Type: INDEX; Schema: public; Owner: questionbox
--

CREATE INDEX questions_user_groups_group_id_e02b4060 ON public.questions_user_groups USING btree (group_id);


--
-- Name: questions_user_groups_user_id_015f9fef; Type: INDEX; Schema: public; Owner: questionbox
--

CREATE INDEX questions_user_groups_user_id_015f9fef ON public.questions_user_groups USING btree (user_id);


--
-- Name: questions_user_user_permissions_permission_id_884e93d1; Type: INDEX; Schema: public; Owner: questionbox
--

CREATE INDEX questions_user_user_permissions_permission_id_884e93d1 ON public.questions_user_user_permissions USING btree (permission_id);


--
-- Name: questions_user_user_permissions_user_id_4e32d12a; Type: INDEX; Schema: public; Owner: questionbox
--

CREATE INDEX questions_user_user_permissions_user_id_4e32d12a ON public.questions_user_user_permissions USING btree (user_id);


--
-- Name: questions_user_username_923f3f9e_like; Type: INDEX; Schema: public; Owner: questionbox
--

CREATE INDEX questions_user_username_923f3f9e_like ON public.questions_user USING btree (username varchar_pattern_ops);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authtoken_token authtoken_token_user_id_35299eff_fk_questions_user_id; Type: FK CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_35299eff_fk_questions_user_id FOREIGN KEY (user_id) REFERENCES public.questions_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_questions_user_id; Type: FK CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_questions_user_id FOREIGN KEY (user_id) REFERENCES public.questions_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: questions_answer questions_answer_author_id_ceb2e333_fk_questions_user_id; Type: FK CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.questions_answer
    ADD CONSTRAINT questions_answer_author_id_ceb2e333_fk_questions_user_id FOREIGN KEY (author_id) REFERENCES public.questions_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: questions_answer questions_answer_question_id_45884d67_fk_questions_question_id; Type: FK CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.questions_answer
    ADD CONSTRAINT questions_answer_question_id_45884d67_fk_questions_question_id FOREIGN KEY (question_id) REFERENCES public.questions_question(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: questions_profile questions_profile_user_id_31082efe_fk_questions_user_id; Type: FK CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.questions_profile
    ADD CONSTRAINT questions_profile_user_id_31082efe_fk_questions_user_id FOREIGN KEY (user_id) REFERENCES public.questions_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: questions_question questions_question_author_id_f53392d1_fk_questions_user_id; Type: FK CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.questions_question
    ADD CONSTRAINT questions_question_author_id_f53392d1_fk_questions_user_id FOREIGN KEY (author_id) REFERENCES public.questions_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: questions_starreditem questions_starredite_content_type_id_87569512_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.questions_starreditem
    ADD CONSTRAINT questions_starredite_content_type_id_87569512_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: questions_starreditem questions_starreditem_user_id_cc32ed93_fk_questions_user_id; Type: FK CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.questions_starreditem
    ADD CONSTRAINT questions_starreditem_user_id_cc32ed93_fk_questions_user_id FOREIGN KEY (user_id) REFERENCES public.questions_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: questions_user_groups questions_user_groups_group_id_e02b4060_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.questions_user_groups
    ADD CONSTRAINT questions_user_groups_group_id_e02b4060_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: questions_user_groups questions_user_groups_user_id_015f9fef_fk_questions_user_id; Type: FK CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.questions_user_groups
    ADD CONSTRAINT questions_user_groups_user_id_015f9fef_fk_questions_user_id FOREIGN KEY (user_id) REFERENCES public.questions_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: questions_user_user_permissions questions_user_user__permission_id_884e93d1_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.questions_user_user_permissions
    ADD CONSTRAINT questions_user_user__permission_id_884e93d1_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: questions_user_user_permissions questions_user_user__user_id_4e32d12a_fk_questions; Type: FK CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.questions_user_user_permissions
    ADD CONSTRAINT questions_user_user__user_id_4e32d12a_fk_questions FOREIGN KEY (user_id) REFERENCES public.questions_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: registration_registrationprofile registration_registr_user_id_5fcbf725_fk_questions; Type: FK CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.registration_registrationprofile
    ADD CONSTRAINT registration_registr_user_id_5fcbf725_fk_questions FOREIGN KEY (user_id) REFERENCES public.questions_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: registration_supervisedregistrationprofile registration_supervi_registrationprofile__0a59f3b2_fk_registrat; Type: FK CONSTRAINT; Schema: public; Owner: questionbox
--

ALTER TABLE ONLY public.registration_supervisedregistrationprofile
    ADD CONSTRAINT registration_supervi_registrationprofile__0a59f3b2_fk_registrat FOREIGN KEY (registrationprofile_ptr_id) REFERENCES public.registration_registrationprofile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

