<template>
	<view class="body">
		<view class="user-set-userinfo-list u-f-ac u-f-jsb">
			<view>头像</view>
			<view class="u-f-ac" @tap="changeimg">
				<image :src="userpic" mode="aspectFill" lazy-load></image>
				<view class="icon iconfont icon-bianji1"></view>
			</view>
		</view>
		<view class="user-set-userinfo-list u-f-ac u-f-jsb">
			<view>昵称</view>
			<view class="u-f-ac">
				<input type="text" v-model="username" />
				<view class="icon iconfont icon-bianji1"></view>
			</view>
		</view>
		<view class="user-set-userinfo-list u-f-ac u-f-jsb">
			<view>性别</view>
			<view class="u-f-ac" @tap="changeOne('sex')">
				<view>{{sex}}</view>
				<view class="icon iconfont icon-bianji1"></view>
			</view>
		</view>
		<view class="user-set-userinfo-list u-f-ac u-f-jsb">
			<view>生日</view>
			<picker mode="date" :value="birthday" :start="startDate" :end="endDate" @change="bindDateChange">
				<view class="u-f-ac">
					<view>{{birthday}}</view>
					<view class="icon iconfont icon-bianji1"></view>
				</view>
			</picker>
		</view>
		<view class="user-set-userinfo-list u-f-ac u-f-jsb">
			<view>情感</view>
			<view class="u-f-ac" @tap="changeOne('qg')">
				<view>{{qg}}</view>
				<view class="icon iconfont icon-bianji1"></view>
			</view>
		</view>
		<view class="user-set-userinfo-list u-f-ac u-f-jsb">
			<view>职业</view>
			<view class="u-f-ac" @tap="changeOne('job')">
				<view>{{job}}</view>
				<view class="icon iconfont icon-bianji1"></view>
			</view>
		</view>
		<view class="user-set-userinfo-list u-f-ac u-f-jsb">
			<view>家乡</view>
			<view class="u-f-ac" @tap="showMulLinkageThreePicker">
				<view>{{pickerText}}</view>
				<view class="icon iconfont icon-bianji1"></view>
			</view>
		</view>
		<button class="user-set-btn" type="primary" @tap="submit">完成
		</button>
		<mpvue-city-picker themeColor="#007AFF" ref="mpvueCityPicker" 
		:pickerValueDefault="cityPickerValueDefault" @onConfirm="onConfirm">
		</mpvue-city-picker>
	</view>
</template>

<script>
	import mpvueCityPicker from '../../components/mpvue-citypicker/mpvueCityPicker.vue'

	let sexArr = ['不限', '男', '女']
	let qgArr = ['未婚', '已婚', '不告诉你']
	let jobArr = ['IT', '老师', '医生', "不告诉你"]

	export default {
		components: {
			mpvueCityPicker
		},
		data() {
			return {
				userpic: "../../static/demo/userpic/11.jpg",
				username: "哈哈哈",
				sex: "不限",
				qg: "未婚",
				job: "IT",
				birthday: "1987-02-07",
				cityPickerValueDefault: [0, 0, 1],
				pickerText: '广东省-广州市-白云区'
			}
		},
		computed: {
			startDate() {
				return this.getDate('start');
			},
			endDate() {
				return this.getDate('end');
			}
		},
		methods: {
			// 三级联动选择
			showMulLinkageThreePicker() {
				this.$refs.mpvueCityPicker.show()
			},
			onConfirm(e) {
				this.pickerText = e.label;
			},
			onBackPress() {
				if (this.$refs.mpvueCityPicker.showPicker) {
					this.$refs.mpvueCityPicker.pickerCancel();
					return true;
				}
			},
			onUnload() {
				if (this.$refs.mpvueCityPicker.showPicker) {
					this.$refs.mpvueCityPicker.pickerCancel()
				}
			},
			bindDateChange(e) {
				this.birthday = e.target.value
			},
			getDate(type) {
				const date = new Date();
				let year = date.getFullYear();
				let month = date.getMonth() + 1;
				let day = date.getDate();

				if (type === 'start') {
					year = year - 60;
				} else if (type === 'end') {
					year = year + 2;
				}
				month = month > 9 ? month : '0' + month;;
				day = day > 9 ? day : '0' + day;
				return `${year}-${month}-${day}`;
			},
			// 单列选择
			changeOne(val) {
				let arr = [];
				switch (val) {
					case 'sex':
						arr = sexArr;
						break;
					case 'qg':
						arr = qgArr;
						break;
					case 'job':
						arr = jobArr;
						break;
				}
				uni.showActionSheet({
					itemList: arr,
					success: (res) => {
						switch (val) {
							case 'sex':
								this.sex = arr[res.tapIndex];
								break;
							case 'qg':
								this.qg = arr[res.tapIndex];
								break;
							case 'job':
								this.job = arr[res.tapIndex];
								break;
						}
					},
					fail: (res) => {
						console.log(res.errMsg);
					}
				});
			},
			// 修改头像
			changeimg() {
				uni.chooseImage({
					count: 1,
					sizeType: ['compressed'],
					success: (res) => {
						// console.log(JSON.stringify(res.tempFilePaths));
						// console.log(res.tempFilePaths[0]);
						this.userpic = res.tempFilePaths[0];
					}
				});
			},
			submit() {

			}
		}
	}
</script>

<style>
	@import "../../common/form.css";

	.user-set-userinfo-list {
		padding: 20rpx;
		border-bottom: 1rpx solid #F4F4F4;
	}

	.user-set-userinfo-list>view:first-child {
		font-size: 30rpx;
		font-weight: bold;
		color: #9B9B9B;
	}

	.user-set-userinfo-list>view:last-child>image {
		width: 80rpx;
		height: 80rpx;
		border-radius: 100%;
	}

	.user-set-userinfo-list>view:last-child>input {
		text-align: right;
	}

	.user-set-userinfo-list>view:last-child>view:last-of-type {
		margin-left: 20rpx;
		color: #9B9B9B;
	}
</style>
