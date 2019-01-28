const routers = [{
        path: '/peppapeppa',
        meta: {
            title: ''
        },
        component: (resolve) => require(['./views/peppapeppa.vue'], resolve)
    },
    {
        path: '/',
        meta: {
            title: ''
        },
        component: (resolve) => require(['./views/index.vue'], resolve)
    }
];
export default routers;